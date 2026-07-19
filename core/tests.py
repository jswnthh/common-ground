from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .data import get_counsellor_by_slug, get_counsellors
from .models import Booking, Counsellor
from .scheduling import MIN_LEAD_TIME, get_available_slots


def next_working_date(counsellor, after_hours=None):
    """First date at least MIN_LEAD_TIME + 1 day out that counsellor works."""
    d = (timezone.now() + MIN_LEAD_TIME + timedelta(days=1)).date()
    for _ in range(14):
        if counsellor["working_hours"].get(d.weekday()):
            return d
        d += timedelta(days=1)
    raise AssertionError("no working day found in the next 14 days")


class AvailabilityTests(TestCase):
    def setUp(self):
        self.counsellor = get_counsellor_by_slug(get_counsellors()[0]["slug"])
        self.date = next_working_date(self.counsellor)

    def test_slots_available_on_a_working_day(self):
        slots = get_available_slots(self.counsellor, self.date)
        self.assertTrue(len(slots) > 0)

    def test_existing_booking_excludes_that_slot(self):
        slots = get_available_slots(self.counsellor, self.date)
        first_slot = slots[0]

        Booking.objects.create(
            counsellor_slug=self.counsellor["slug"],
            client_name="Existing Client",
            client_email="existing@example.com",
            mode="online",
            start_at=first_slot,
            end_at=first_slot + timedelta(minutes=50),
        )

        remaining = get_available_slots(self.counsellor, self.date)
        self.assertNotIn(first_slot, remaining)


class BookingViewTests(TestCase):
    def setUp(self):
        self.counsellor = get_counsellor_by_slug(get_counsellors()[0]["slug"])
        self.date = next_working_date(self.counsellor)
        self.slot = get_available_slots(self.counsellor, self.date)[0]

    def _post_data(self):
        return {
            "counsellor_slug": self.counsellor["slug"],
            "date": self.date.isoformat(),
            "time": self.slot.strftime("%H:%M:%S"),
            "mode": "online",
            "client_name": "Test Client",
            "client_email": "client@example.com",
        }

    def test_prefills_counsellor_from_query_param(self):
        response = self.client.get(reverse("book") + f"?counsellor={self.counsellor['slug']}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.counsellor["slug"])

    def test_post_creates_a_booking(self):
        response = self.client.post(reverse("book"), self._post_data())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.get()
        self.assertEqual(booking.counsellor_slug, self.counsellor["slug"])
        self.assertEqual(response.url, reverse("book_confirmed", args=[booking.pk]))

    def test_duplicate_post_for_same_slot_is_rejected(self):
        first = self.client.post(reverse("book"), self._post_data())
        self.assertEqual(first.status_code, 302)

        second = self.client.post(reverse("book"), self._post_data())
        self.assertEqual(second.status_code, 200)  # re-rendered form, not a 500
        self.assertEqual(Booking.objects.count(), 1)


class CounsellorAdminPermissionTests(TestCase):
    """A non-superuser staff account tied to a Counsellor via `.user` should
    only ever see/edit its own row in admin — groundwork for a future
    counsellor self-edit login (see CounsellorAdmin in core/admin.py)."""

    def setUp(self):
        User = get_user_model()
        self.mine = Counsellor.objects.create(
            slug="test-own", name="Own Counsellor", credentials="Test", location="Testville",
        )
        self.other = Counsellor.objects.create(
            slug="test-other", name="Other Counsellor", credentials="Test", location="Testville",
        )
        self.user = User.objects.create_user(username="counsellor1", password="pw", is_staff=True)
        self.mine.user = self.user
        self.mine.save()
        for codename in ("view_counsellor", "change_counsellor"):
            self.user.user_permissions.add(Permission.objects.get(codename=codename))
        self.client.force_login(self.user)

    def test_changelist_only_shows_own_counsellor(self):
        response = self.client.get(reverse("admin:core_counsellor_changelist"))
        self.assertEqual(response.status_code, 200)
        result_list = response.context["cl"].result_list
        self.assertEqual(list(result_list), [self.mine])

    def test_other_counsellors_change_form_is_forbidden(self):
        # Not in this user's filtered queryset, so Django admin treats it the
        # same as a nonexistent object: a redirect back to the changelist,
        # not a 403 — either way, the other counsellor's data is unreachable.
        response = self.client.get(reverse("admin:core_counsellor_change", args=[self.other.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("admin:index"))

    def test_can_edit_own_counsellor(self):
        url = reverse("admin:core_counsellor_change", args=[self.mine.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        post_data = {
            "name": "Updated Name",
            "slug": self.mine.slug,
            "credentials": self.mine.credentials,
            "location": self.mine.location,
            "photo_placeholder": "images/face_1.png",
            "languages": "[]",
            "modes": "[]",
            "intro": "Test intro.",
            "bio": "Test bio.",
            "modalities": "[]",
            "fee_note": "",
            "hour_blocks-TOTAL_FORMS": "0",
            "hour_blocks-INITIAL_FORMS": "0",
            "hour_blocks-MIN_NUM_FORMS": "0",
            "hour_blocks-MAX_NUM_FORMS": "1000",
            "specialty_links-TOTAL_FORMS": "0",
            "specialty_links-INITIAL_FORMS": "0",
            "specialty_links-MIN_NUM_FORMS": "0",
            "specialty_links-MAX_NUM_FORMS": "1000",
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        self.mine.refresh_from_db()
        self.assertEqual(self.mine.name, "Updated Name")

    def test_cannot_add_or_delete_counsellors(self):
        add_response = self.client.get(reverse("admin:core_counsellor_add"))
        self.assertEqual(add_response.status_code, 403)

        delete_response = self.client.get(reverse("admin:core_counsellor_delete", args=[self.mine.pk]))
        self.assertEqual(delete_response.status_code, 403)

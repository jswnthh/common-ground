"""DB-backed accessors for the site's content: topics, services, and the
counsellors they map to. Counsellor/topic/service content now lives in real
tables (see core/models.py: ServiceCategory, Topic, Counsellor,
CounsellorWorkingHours, CounsellorSpecialty) editable via Django admin — this
module is a thin query layer that reshapes those rows into the same plain-dict
shapes views.py/forms.py/scheduling.py/templates/JS have always consumed, so
nothing downstream needs to know the data used to be static Python literals.

Every function here queries fresh each call (never cache at module import
time) so admin edits show up immediately, without a server restart.
"""

from django.templatetags.static import static

from .models import Counsellor, ServiceCategory, Topic


def get_topic_labels():
    """slug -> display label, across every topic in every category."""
    return {t.slug: t.label for t in Topic.objects.select_related("category")}


def get_services():
    """service slug -> {name, eyebrow, intro, topics: [slug, ...]}."""
    return {
        category.slug: {
            "name": category.name,
            "eyebrow": category.eyebrow,
            "intro": category.intro,
            "topics": [t.slug for t in category.topics.all()],
        }
        for category in ServiceCategory.objects.prefetch_related("topics")
    }


def _resolve_photo(counsellor):
    return counsellor.photo.url if counsellor.photo else static(counsellor.photo_placeholder)


def _working_hours_dict(counsellor):
    hours = {}
    for block in counsellor.hour_blocks.all():
        hours.setdefault(block.weekday, []).append(
            (block.start_time.strftime("%H:%M"), block.end_time.strftime("%H:%M"))
        )
    return hours


def _specialties_dict(counsellor):
    return {link.topic.slug: link.level for link in counsellor.specialty_links.all()}


def _to_dict(counsellor):
    return {
        "slug": counsellor.slug,
        "name": counsellor.name,
        "credentials": counsellor.credentials,
        "photo": _resolve_photo(counsellor),
        "is_active": counsellor.is_active,
        "modes": counsellor.modes,
        "languages": counsellor.languages,
        "location": counsellor.location,
        "intro": counsellor.intro,
        "bio": counsellor.bio,
        "modalities": counsellor.modalities,
        "specialties": _specialties_dict(counsellor),
        "fee_note": counsellor.fee_note,
        "working_hours": _working_hours_dict(counsellor),
    }


def _counsellor_queryset():
    return Counsellor.objects.prefetch_related("hour_blocks", "specialty_links__topic")


def get_counsellors():
    return [_to_dict(c) for c in _counsellor_queryset()]


def get_counsellor_by_slug(slug):
    counsellor = _counsellor_queryset().filter(slug=slug).first()
    return _to_dict(counsellor) if counsellor else None

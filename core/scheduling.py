"""Slot generation: a counsellor's real availability for a given date."""

from datetime import datetime, time, timedelta

from django.utils import timezone

from .calendar_sync import get_busy_intervals
from .models import Booking

SESSION_LENGTH_MINUTES = 50
SLOT_STEP_MINUTES = 60  # slots start on the hour, leaving a 10-minute gap
BOOKING_WINDOW_DAYS = 21  # rolling 3-week booking horizon
MIN_LEAD_TIME = timedelta(hours=2)
SESSION_FEE_DISPLAY = "₹1,500"  # cosmetic display only; no payment processing


def get_available_slots(counsellor, date_):
    """Return a sorted list of tz-aware datetimes counsellor is free to start
    a session at on date_, honouring working hours, existing bookings, and
    (once real) external calendar busy time."""
    windows = counsellor.get("working_hours", {}).get(date_.weekday(), [])
    if not windows:
        return []

    now = timezone.now()
    horizon = now + timedelta(days=BOOKING_WINDOW_DAYS)

    candidates = []
    for start_str, end_str in windows:
        window_start = timezone.make_aware(datetime.combine(date_, time.fromisoformat(start_str)))
        window_end = timezone.make_aware(datetime.combine(date_, time.fromisoformat(end_str)))
        cursor = window_start
        while cursor + timedelta(minutes=SESSION_LENGTH_MINUTES) <= window_end:
            if now + MIN_LEAD_TIME <= cursor <= horizon:
                candidates.append(cursor)
            cursor += timedelta(minutes=SLOT_STEP_MINUTES)

    if not candidates:
        return []

    day_start = timezone.make_aware(datetime.combine(date_, time.min))
    day_end = day_start + timedelta(days=1)
    booked = list(
        Booking.objects.filter(
            counsellor_slug=counsellor["slug"],
            status=Booking.Status.CONFIRMED,
            start_at__lt=day_end,
            end_at__gt=day_start,
        ).values_list("start_at", "end_at")
    )
    busy = get_busy_intervals(counsellor["slug"], date_)  # stub -> [] today

    blocked = booked + busy

    def is_free(slot_start):
        slot_end = slot_start + timedelta(minutes=SESSION_LENGTH_MINUTES)
        return not any(slot_start < b_end and b_start < slot_end for b_start, b_end in blocked)

    return sorted(c for c in candidates if is_free(c))

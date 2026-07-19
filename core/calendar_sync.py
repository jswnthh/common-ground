"""Calendar-sync seam for Google/Outlook calendars.

No live OAuth integration exists yet — no app is registered with either
provider, and there is no counsellor-facing "connect your calendar" flow
(counsellors aren't site users; there's no login system for them). Both
functions below are the only place a real integration would plug in: they
check CalendarAccount.is_connected, log what *would* happen, and no-op.
Callers (core/scheduling.py, core/views.py) don't need to know this.
"""

import logging

from .models import CalendarAccount

logger = logging.getLogger(__name__)


def get_busy_intervals(counsellor_slug, date_):
    """Return [(start_dt, end_dt), ...] the counsellor is busy on their
    external calendar for the given date. Stubbed: always [] today."""
    account = CalendarAccount.objects.filter(counsellor_slug=counsellor_slug, is_connected=True).first()
    if account is None:
        return []
    logger.info(
        "calendar_sync stub: get_busy_intervals(%s, %s) — provider=%s, no live call made",
        counsellor_slug, date_, account.provider,
    )
    return []


def create_calendar_event(booking):
    """Would create an event on the counsellor's external calendar for a
    confirmed booking. Stubbed: logs and returns None (no calendar_event_id)."""
    account = CalendarAccount.objects.filter(counsellor_slug=booking.counsellor_slug, is_connected=True).first()
    if account is None:
        logger.info(
            "calendar_sync stub: no connected calendar for %s, booking #%s",
            booking.counsellor_slug, booking.pk,
        )
        return None
    logger.info(
        "calendar_sync stub: create_calendar_event(booking=#%s, provider=%s) — no live call made",
        booking.pk, account.provider,
    )
    return None

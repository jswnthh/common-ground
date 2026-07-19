# Counsellor content & photo intake

Send this to each counsellor to fill in. Everything below maps directly to a field on the live site — once you have answers for a counsellor, hand them
back and they get typed straight into `core/data.py` (or emailed to me to do
it). Sections 1–8 are simple copy; Section 9 (specialties) and Section 10
(availability) need a bit more structure since they drive the matching
algorithm and the booking calendar — templates for both are included below.

---

## 1. Full name

As it should appear on the site, including any title/prefix.

> Example: **Dr. Meera Iyer**

## 2. Credentials line

One short line shown directly under the name everywhere on the site.

> Example: **Clinical Psychologist, PhD**
> Example: **Licensed Marriage & Family Therapist**

## 3. Headshot photo

- **Framing:** head-and-shoulders, face roughly in the top third of the frame
  (photos get cropped into a circle centred on the top of the image, so keep
  the face high and centred — not a full-body or wide shot).
- **Background:** neutral or softly blurred, consistent tone across everyone
  if possible (plain wall, soft outdoor blur, etc.) — avoid busy backgrounds.
- **Light:** natural, even light on the face. No hard shadows, no heavy
  filters, no sunglasses.
- **Resolution:** at least **600×600px**, square or near-square. A clear
  phone photo is completely fine — it just needs to not be blurry or
  pixelated once resized.
- **Recency:** within the last ~2 years, so it matches how the counsellor
  actually looks when a client meets them.
- **File:** JPG or PNG, named `firstname-lastname.jpg` (e.g.
  `meera-iyer.jpg`).

## 4. Location

City they primarily see clients from (e.g. **Bengaluru**), or **Remote** if
they only work online.

## 5. Session modes offered

Choose one: **Online only** / **In-person only** / **Both online and in-person**

## 6. Languages spoken

List all, in order of fluency/preference (e.g. **English, Hindi, Punjabi**).

## 7. One-line intro

The short teaser sentence shown in listings and match cards. Third person,
warm but *specific* — who they help and with what. Avoid generic lines like
"passionate about helping people."

- Aim for **15–25 words**.
- Example: *"Works with leaders and teams carrying stress, burnout and
  anxiety that follows them home."*

## 8. Full bio

One paragraph (**3–5 sentences**), third person. Cover:

1. Background — years of experience, setting, training.
2. Approach/style — how they actually work with clients.
3. Who/what they specialise in.
4. One distinguishing detail if there is one (leads workshops, specific
   population, notable focus).

> Example: *"Meera has spent twelve years helping professionals and
> executives recognise burnout before it becomes a crisis. She blends CBT
> with a grounded, practical style — clients often say she's the person who
> finally makes their stress make sense. She also leads Common Ground's
> corporate wellness workshops."*

Also list **therapeutic modalities/approaches** separately as short tags
(e.g. `CBT`, `Acceptance & Commitment Therapy`, `Systemic therapy`,
`Emotionally Focused Therapy`) — these show as pills, not prose.

---

## 9. Specialties (Primary / Secondary)

This is the field the "find your best-fit counsellor" matching on the
service pages actually runs on, so it needs to come from the fixed list
below rather than free text. Ask the counsellor to mark each topic they work
with as either:

- **Primary** — a core specialty, what they're most known for.
- **Secondary** — comfortable working with it, but not their main focus.

They can pick from more than one category below if their practice spans
multiple services (e.g. a therapist doing both individual anxiety work and
corporate workshops).

### Individual therapy
☐ Anxiety · ☐ Low mood & depression · ☐ Burnout · ☐ Self-esteem ·
☐ Life transitions · ☐ Grief & loss · ☐ Identity · ☐ Anger management ·
☐ Sleep difficulties · ☐ Perfectionism

### Couples & family
☐ Communication breakdown · ☐ Trust & infidelity · ☐ Parenting conflict ·
☐ Blended family dynamics · ☐ Pre-marital counselling · ☐ Intimacy issues ·
☐ Separation & divorce · ☐ Family estrangement · ☐ Conflict resolution ·
☐ Life-stage transitions

### Corporate wellness
☐ Stress & burnout · ☐ Team conflict · ☐ Leadership pressure ·
☐ Work-life balance · ☐ Anxiety at work · ☐ Communication skills ·
☐ Change & restructuring · ☐ Psychological safety · ☐ Employee engagement ·
☐ Manager support

### Academic workshops
☐ Exam stress · ☐ Academic pressure · ☐ Time management · ☐ Social anxiety ·
☐ Peer relationships · ☐ Imposter syndrome · ☐ Study-life balance ·
☐ School-to-uni transitions · ☐ Building confidence · ☐ Asking for help

*(Mark each selected box "P" for primary or "S" for secondary instead of a
plain tick.)*

---

## 10. Weekly availability

Plain-language weekly schedule, **in IST (Indian Standard Time)** — the site
assumes IST throughout. List working windows per day; write "Off" for days
they don't see clients.

> Example:
> Monday: 9:00 AM–1:00 PM, 2:00 PM–5:00 PM
> Tuesday: 9:00 AM–1:00 PM, 2:00 PM–5:00 PM
> Wednesday: 9:00 AM–1:00 PM, 2:00 PM–5:00 PM
> Thursday: 9:00 AM–1:00 PM, 2:00 PM–5:00 PM
> Friday: 9:00 AM–1:00 PM, 2:00 PM–5:00 PM
> Saturday: Off
> Sunday: Off

For context (they don't need to specify this): sessions are booked in
50-minute slots starting on the hour, so a "9:00 AM–1:00 PM" window offers
four bookable start times (9, 10, 11, 12).

## 11. Session fee *(optional)*

Not required — the site currently shows one flat rate for every counsellor.
If you want per-counsellor pricing later, note their rate here and flag it
to me; it's a small follow-up change, not something already wired in.

---

## Quick-fill template (copy per counsellor)

```
Name:
Credentials:
Photo: [attached / link]
Location:
Modes:
Languages:
Intro (one line):
Bio (paragraph):
Modalities:
Specialties (P/S):
Availability (Mon–Sun, IST):
Fee (optional):
```

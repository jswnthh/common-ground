# Seeds the site's topic taxonomy and the 7 real counsellor profiles that
# previously lived as static literals in core/data.py. The content below is a
# frozen copy of that data at the time of this migration — migrations must
# stay replayable even after core/data.py itself changes, so nothing here
# imports from the app; it uses the historical models via apps.get_model().

from datetime import time

from django.db import migrations

# service category slug -> (name, eyebrow, intro, order)
SERVICE_CATEGORIES = [
    (
        "individual-therapy",
        "Individual therapy",
        "One-to-one",
        "Weekly, one-to-one sessions for anxiety, low mood, burnout and "
        "everything harder to name. We match you with the counsellor whose "
        "experience fits what you're carrying, not whoever happens to be free.",
    ),
    (
        "couples-family",
        "Couples & family",
        "Together",
        "Structured, judgment-free sessions to rebuild communication and "
        "trust, grounded in systemic and emotionally focused therapy — "
        "for couples, parents and families.",
    ),
    (
        "corporate-wellness",
        "Corporate wellness",
        "For organisations",
        "On-site and virtual workshops helping teams manage stress and "
        "burnout, with confidential one-to-one support available for "
        "employees who need it. Built for HR teams and managers, not just "
        "individuals.",
    ),
    (
        "academic-workshops",
        "Academic workshops",
        "For students",
        "Practical, age-appropriate workshops for schools and universities "
        "on exam pressure, emotional resilience and asking for help — "
        "delivered by qualified counsellors, not generic wellbeing content.",
    ),
]

# category slug -> ordered list of (topic slug, label)
TOPICS_BY_CATEGORY = {
    "individual-therapy": [
        ("anxiety", "Anxiety"),
        ("low-mood", "Low mood & depression"),
        ("personal-burnout", "Burnout"),
        ("self-esteem", "Self-esteem"),
        ("life-transitions", "Life transitions"),
        ("grief-loss", "Grief & loss"),
        ("identity", "Identity"),
        ("anger-management", "Anger management"),
        ("sleep-difficulties", "Sleep difficulties"),
        ("perfectionism", "Perfectionism"),
    ],
    "couples-family": [
        ("communication-breakdown", "Communication breakdown"),
        ("trust-infidelity", "Trust & infidelity"),
        ("parenting-conflict", "Parenting conflict"),
        ("blended-family", "Blended family dynamics"),
        ("premarital-counselling", "Pre-marital counselling"),
        ("intimacy-issues", "Intimacy issues"),
        ("separation-divorce", "Separation & divorce"),
        ("family-estrangement", "Family estrangement"),
        ("conflict-resolution", "Conflict resolution"),
        ("life-stage-transitions", "Life-stage transitions"),
    ],
    "corporate-wellness": [
        ("stress-burnout", "Stress & burnout"),
        ("team-conflict", "Team conflict"),
        ("leadership-pressure", "Leadership pressure"),
        ("work-life-balance", "Work-life balance"),
        ("workplace-anxiety", "Anxiety at work"),
        ("communication-skills", "Communication skills"),
        ("change-restructuring", "Change & restructuring"),
        ("psychological-safety", "Psychological safety"),
        ("employee-engagement", "Employee engagement"),
        ("manager-support", "Manager support"),
    ],
    "academic-workshops": [
        ("exam-stress", "Exam stress"),
        ("academic-pressure", "Academic pressure"),
        ("time-management", "Time management"),
        ("social-anxiety", "Social anxiety"),
        ("peer-relationships", "Peer relationships"),
        ("imposter-syndrome", "Imposter syndrome"),
        ("study-life-balance", "Study-life balance"),
        ("school-transitions", "School-to-uni transitions"),
        ("building-confidence", "Building confidence"),
        ("asking-for-help", "Asking for help"),
    ],
}

COUNSELLORS = [
    {
        "slug": "aadhithya-m",
        "name": "Ms. Aadhithya M",
        "credentials": "Counselling Psychologist",
        "photo_placeholder": "images/face_1.png",
        "modes": ["online", "in-person"],
        "languages": ["Tamil", "English"],
        "location": "Palani",
        "intro": "A space to share your vulnerability — to be held and heard.",
        "bio": (
            "Aadhithya M is a Counselling Psychologist who works with "
            "individuals navigating emotional distress, trauma, relationship "
            "concerns, life transitions, and mental health challenges. She is "
            "known for her thoughtful, empathetic, and personalised approach, "
            "helping clients feel genuinely heard, understood, and respected "
            "while making sense of their experiences. Her work integrates "
            "evidence-based psychological interventions with practical, "
            "tailored strategies that support meaningful and lasting change."
        ),
        "modalities": [
            "CBT",
            "Behaviour Therapy (BT)",
            "Acceptance & Commitment Therapy (ACT)",
            "Dialectical Behaviour Therapy (DBT)",
            "Solution-Focused Brief Therapy (SFBT)",
            "Motivational Interviewing (MI)",
            "Mindfulness-Based Interventions",
            "Gestalt techniques",
            "Psychodynamic principles",
            "Person-Centred Therapy",
        ],
        "specialties": {
            "anxiety": 2, "low-mood": 2, "personal-burnout": 1, "self-esteem": 2,
            "life-transitions": 2, "grief-loss": 2, "identity": 2, "anger-management": 2,
            "sleep-difficulties": 2, "perfectionism": 2, "communication-breakdown": 2,
            "trust-infidelity": 2, "parenting-conflict": 2, "blended-family": 2,
            "premarital-counselling": 2, "intimacy-issues": 1, "separation-divorce": 2,
            "family-estrangement": 2, "conflict-resolution": 2, "life-stage-transitions": 2,
            "stress-burnout": 1, "team-conflict": 1, "leadership-pressure": 2,
            "work-life-balance": 2, "workplace-anxiety": 2, "communication-skills": 2,
            "change-restructuring": 2, "psychological-safety": 2, "employee-engagement": 2,
            "manager-support": 1, "exam-stress": 2, "academic-pressure": 2,
            "time-management": 2, "social-anxiety": 2, "peer-relationships": 2,
            "imposter-syndrome": 2, "study-life-balance": 2, "school-transitions": 2,
            "building-confidence": 2, "asking-for-help": 2,
        },
        "fee_note": "₹2,000 per session",
        "working_hours": {
            0: [("08:00", "20:00")], 1: [("08:00", "20:00")], 2: [("08:00", "20:00")],
            3: [("08:00", "20:00")], 4: [("08:00", "20:00")], 5: [("08:00", "20:00")],
            6: [("08:00", "20:00")],
        },
    },
    {
        "slug": "divya-shri",
        "name": "Ms. Divya Shri S",
        "credentials": "Counselling Psychologist, MSc",
        "photo_placeholder": "images/face_2.png",
        "modes": ["online", "in-person"],
        "languages": ["Tamil", "English"],
        "location": "Chennai",
        "intro": (
            "Creates a safe, non-judgmental space for adolescents, young "
            "adults, individuals and couples to heal, grow and strengthen "
            "relationships."
        ),
        "bio": (
            "Divya Shri is a Counselling Psychologist who creates a safe, "
            "compassionate, and non-judgmental space where adolescents, young "
            "adults, parents, individuals, and couples can explore their "
            "thoughts, emotions, and relationships with honesty and "
            "confidence. She supports clients navigating emotional "
            "challenges, anxiety, self-esteem concerns, relationship and "
            "premarital concerns, parenting challenges, and life "
            "transitions. With a warm, collaborative, and evidence-informed "
            "approach, she helps clients gain deeper self-awareness, build "
            "emotional resilience, strengthen relationships, and create "
            "meaningful, lasting change."
        ),
        "modalities": [
            "Person-Centred Therapy", "CBT", "Transactional Analysis (TA)",
            "Solution-Focused Brief Therapy (SFBT)", "Strengths-Based Approach",
            "Trauma-Informed Care", "Mindfulness-Based Interventions", "Psychoeducation",
        ],
        "specialties": {
            "self-esteem": 2, "anxiety": 1, "low-mood": 1, "personal-burnout": 1,
            "communication-breakdown": 2, "communication-skills": 2, "asking-for-help": 2,
            "premarital-counselling": 2, "blended-family": 1, "parenting-conflict": 1,
            "psychological-safety": 1, "exam-stress": 2, "academic-pressure": 2,
            "time-management": 2, "social-anxiety": 2, "peer-relationships": 2,
            "study-life-balance": 2, "school-transitions": 2, "building-confidence": 2,
            "imposter-syndrome": 1,
        },
        "fee_note": "₹800 for working professionals, ₹600 for school students",
        "working_hours": {
            0: [("19:30", "22:30")], 1: [("19:30", "22:30")], 2: [("19:30", "22:30")],
            3: [("19:30", "22:30")], 4: [("19:30", "22:30")], 5: [("10:00", "22:00")],
            6: [("10:00", "22:00")],
        },
    },
    {
        "slug": "jayalakshmi-esakki",
        "name": "Jayalakshmi Esakki",
        "credentials": "Counselling Psychologist",
        "photo_placeholder": "images/face_3.png",
        "modes": ["online", "in-person"],
        "languages": ["English", "Tamil"],
        "location": "Chennai",
        "intro": (
            "Helps individuals who feel stuck or overwhelmed reconnect with "
            "themselves and start living, not just coping."
        ),
        "bio": (
            "Jayalakshmi Esakki is a counselling psychologist with experience "
            "across school, clinical, and community mental health settings, "
            "including work with children, adolescents, and adults. She "
            "takes a warm, practical and client-centered approach, helping "
            "individuals understand their emotions, build resilience and "
            "move from simply coping to truly living. Her work focuses on "
            "areas such as student well-being, emotional regulation, "
            "relationship concerns, and career-related stress."
        ),
        "modalities": [
            "Acceptance & Commitment Therapy (ACT)", "Behaviour Therapy (BT)",
            "Solution-Focused Brief Therapy (SFBT)", "Problem-Solving Therapy",
            "Mindfulness-Based Cognitive Therapy (MBCT)",
        ],
        "specialties": {
            "anxiety": 2, "low-mood": 2, "personal-burnout": 2, "self-esteem": 2,
            "sleep-difficulties": 2, "life-transitions": 1, "grief-loss": 1, "identity": 1,
            "anger-management": 1, "perfectionism": 1, "communication-breakdown": 2,
            "trust-infidelity": 2, "parenting-conflict": 2, "intimacy-issues": 2,
            "premarital-counselling": 1, "conflict-resolution": 1, "life-stage-transitions": 1,
            "stress-burnout": 2, "team-conflict": 2, "leadership-pressure": 2,
            "work-life-balance": 2, "employee-engagement": 2, "change-restructuring": 1,
            "exam-stress": 2, "academic-pressure": 2, "time-management": 2,
            "social-anxiety": 2, "peer-relationships": 2, "imposter-syndrome": 2,
            "study-life-balance": 2, "building-confidence": 2,
        },
        "fee_note": "₹500 per session (subject to change)",
        "working_hours": {
            0: [("17:00", "21:00")], 1: [("17:00", "21:00")], 2: [("17:00", "21:00")],
            3: [("17:00", "21:00")], 4: [("17:00", "21:00")], 5: [("10:00", "13:00")],
        },
    },
    {
        "slug": "rakshena",
        "name": "AR. Rakshena",
        "credentials": "Counselling Psychologist",
        "photo_placeholder": "images/face_4.png",
        "modes": ["online", "in-person"],
        "languages": ["English", "Tamil"],
        "location": "Chennai",
        "intro": (
            "Works with children, adolescents and parents to build emotional "
            "resilience, strengthen relationships and navigate developmental "
            "and behavioural challenges."
        ),
        "bio": (
            "Rakshena is a Counselling Psychology postgraduate with "
            "experience in early childhood education and child development. "
            "She has worked closely with preschool children and families, "
            "supporting their emotional, behavioural, and developmental "
            "needs. She also holds a certification in Dyslexia, enabling her "
            "to better understand and support children with diverse "
            "learning needs. Her approach is warm, child-centred, and "
            "focused on fostering emotional well-being and healthy "
            "development."
        ),
        "modalities": [
            "Child-Centred Counselling", "CBT", "Solution-Focused Brief Therapy (SFBT)",
            "Play-Based Interventions", "Psychoeducation", "Parent Guidance",
        ],
        "specialties": {
            "self-esteem": 2, "life-transitions": 2, "identity": 2, "anxiety": 1,
            "low-mood": 1, "anger-management": 1, "parenting-conflict": 2,
            "conflict-resolution": 1, "life-stage-transitions": 1, "building-confidence": 2,
            "peer-relationships": 2, "school-transitions": 2, "asking-for-help": 2,
            "academic-pressure": 1, "exam-stress": 1, "social-anxiety": 1,
            "study-life-balance": 1,
        },
        "fee_note": "₹800 per session",
        "working_hours": {
            0: [("18:00", "21:00")], 3: [("18:00", "21:00")], 5: [("10:00", "18:00")],
            6: [("10:00", "18:00")],
        },
    },
    {
        "slug": "shaffran",
        "name": "Mrs. Shaffran R Ulfath",
        "credentials": "Counselling Psychologist",
        "photo_placeholder": "images/face_5.png",
        "modes": ["online"],
        "languages": ["English", "Tamil"],
        "location": "Dubai, UAE",
        "intro": "Passionate about creating safe spaces for healing, self-discovery and growth.",
        "bio": (
            "Shaffran is a counselling psychologist dedicated to helping "
            "individuals navigate challenges such as anxiety, stress, grief, "
            "and relationship concerns. She provides a safe, confidential, "
            "and non-judgmental space where clients can openly express their "
            "thoughts and emotions. Using a compassionate and "
            "client-centered approach, she tailors each session to the "
            "unique needs of the individual, empowering them with practical "
            "coping strategies, greater self-awareness, and emotional "
            "resilience."
        ),
        "modalities": [
            "CBT", "Mindfulness-Based Cognitive Therapy (MBCT)",
            "Dialectical Behaviour Therapy (DBT)", "Solution-Focused Brief Therapy (SFBT)",
            "Acceptance & Commitment Therapy (ACT)", "Narrative Therapy", "Exposure Therapy",
        ],
        "specialties": {
            "anxiety": 2, "personal-burnout": 2, "self-esteem": 2, "life-transitions": 2,
            "identity": 2, "perfectionism": 2, "low-mood": 1, "grief-loss": 1,
            "anger-management": 1, "sleep-difficulties": 1, "academic-pressure": 2,
            "school-transitions": 2, "exam-stress": 2, "peer-relationships": 2,
            "social-anxiety": 2, "building-confidence": 2, "study-life-balance": 2,
            "parenting-conflict": 1, "premarital-counselling": 2, "communication-breakdown": 2,
            "conflict-resolution": 2, "life-stage-transitions": 2, "trust-infidelity": 1,
            "intimacy-issues": 1, "separation-divorce": 1, "work-life-balance": 2,
            "stress-burnout": 2, "psychological-safety": 2, "communication-skills": 2,
            "leadership-pressure": 1, "manager-support": 1, "team-conflict": 1,
        },
        "fee_note": "AED/INR 575 per session",
        "working_hours": {
            0: [("11:00", "13:00"), ("17:00", "22:00")],
            1: [("11:00", "13:00"), ("17:00", "22:00")],
            2: [("11:00", "13:00"), ("17:00", "22:00")],
            3: [("11:00", "13:00"), ("17:00", "22:00")],
            4: [("11:00", "13:00"), ("17:00", "22:00")],
        },
    },
    {
        "slug": "thara",
        "name": "Ms. Tharaniswari M",
        "credentials": "Counselling Psychologist / Student Counsellor",
        "photo_placeholder": "images/face_6.png",
        "modes": ["online", "in-person"],
        "languages": ["Tamil", "English"],
        "location": "Chennai",
        "intro": (
            "Works with adolescents, young adults and adults to navigate "
            "stress, relationships and life's transitions with confidence."
        ),
        "bio": (
            "Thara holds an M.Sc. in Counselling Psychology and has 1.7 "
            "years of experience as a Student Counsellor, along with 2 years "
            "of private counselling practice. Her work primarily focuses on "
            "adolescents and young adults, integrating a solution-focused "
            "approach with academic enhancement to address emotional, "
            "behavioural, and educational concerns. She specializes in "
            "student counselling, soft skills training, and Faculty "
            "Development Programmes (FDPs), supporting both students and "
            "educators in fostering psychological well-being and personal "
            "effectiveness."
        ),
        "modalities": [
            "CBT", "Solution-Focused Brief Therapy (SFBT)", "Person-Centred Therapy",
            "Positive Psychology", "Strengths-Based Counselling", "Psychoeducation",
            "Acceptance & Commitment Therapy (ACT)",
        ],
        "specialties": {
            "anxiety": 2, "low-mood": 2, "personal-burnout": 2, "self-esteem": 2,
            "life-transitions": 2, "grief-loss": 2, "identity": 2, "anger-management": 2,
            "perfectionism": 1, "communication-breakdown": 2, "trust-infidelity": 1,
            "parenting-conflict": 2, "blended-family": 2, "premarital-counselling": 2,
            "intimacy-issues": 1, "separation-divorce": 1, "family-estrangement": 1,
            "conflict-resolution": 2, "life-stage-transitions": 2, "stress-burnout": 2,
            "team-conflict": 2, "leadership-pressure": 1, "work-life-balance": 1,
            "workplace-anxiety": 2, "communication-skills": 2, "change-restructuring": 2,
            "psychological-safety": 2, "employee-engagement": 2, "manager-support": 2,
            "exam-stress": 2, "academic-pressure": 2, "time-management": 2,
            "social-anxiety": 2, "peer-relationships": 2, "imposter-syndrome": 2,
            "study-life-balance": 2, "school-transitions": 2, "building-confidence": 2,
            "asking-for-help": 2,
        },
        "fee_note": "₹1,000 per session (negotiable)",
        "working_hours": {
            0: [("17:00", "22:00")], 1: [("17:00", "22:00")], 2: [("17:00", "22:00")],
            3: [("17:00", "22:00")], 4: [("17:00", "22:00")],
        },
    },
    {
        "slug": "yasotha-natarajan",
        "name": "Ms. Yasotha Natarajan",
        "credentials": "Counselling Psychologist, MSc | School Counsellor",
        "photo_placeholder": "images/face_7.png",
        "modes": ["online", "in-person"],
        "languages": ["Tamil", "English"],
        "location": "Coimbatore",
        "intro": (
            "Dedicated to empowering individuals with the skills and support "
            "needed to lead emotionally healthy lives."
        ),
        "bio": (
            "Yasotha Natarajan is a Counselling Psychologist dedicated to "
            "providing a safe, supportive, and confidential space where "
            "individuals can explore their thoughts, emotions, and life "
            "experiences without fear of judgment. She works with children, "
            "adolescents, young adults, and adults experiencing anxiety, "
            "stress, emotional difficulties, relationship concerns, "
            "self-esteem issues, behavioural challenges, and life "
            "transitions. Using an eclectic, evidence-based therapeutic "
            "approach, she tailors counselling to each individual's unique "
            "needs, helping them build self-awareness, resilience, and "
            "emotional wellbeing."
        ),
        "modalities": [
            "Eclectic Therapy", "CBT", "Solution-Focused Brief Therapy (SFBT)",
            "Narrative Therapy", "Art Therapy", "Transactional Analysis (TA)",
            "Psychoeducation", "Strengths-Based Counselling",
        ],
        "specialties": {
            "anxiety": 2, "personal-burnout": 2, "self-esteem": 2, "life-transitions": 2,
            "low-mood": 1, "anger-management": 1, "perfectionism": 1, "identity": 1,
            "exam-stress": 2, "academic-pressure": 2, "time-management": 2,
            "social-anxiety": 2, "building-confidence": 2, "peer-relationships": 2,
            "study-life-balance": 2, "communication-breakdown": 2, "conflict-resolution": 2,
            "life-stage-transitions": 2,
        },
        "fee_note": "",
        "working_hours": {
            0: [("18:00", "21:00")], 1: [("18:00", "21:00")], 2: [("18:00", "21:00")],
            3: [("18:00", "21:00")], 4: [("18:00", "21:00")], 5: [("18:00", "21:00")],
            6: [("11:00", "17:00")],
        },
    },
]


def _time(hhmm):
    h, m = hhmm.split(":")
    return time(int(h), int(m))


def seed_data(apps, schema_editor):
    ServiceCategory = apps.get_model("core", "ServiceCategory")
    Topic = apps.get_model("core", "Topic")
    Counsellor = apps.get_model("core", "Counsellor")
    CounsellorWorkingHours = apps.get_model("core", "CounsellorWorkingHours")
    CounsellorSpecialty = apps.get_model("core", "CounsellorSpecialty")

    categories_by_slug = {}
    for order, (slug, name, eyebrow, intro) in enumerate(SERVICE_CATEGORIES):
        categories_by_slug[slug] = ServiceCategory.objects.create(
            slug=slug, name=name, eyebrow=eyebrow, intro=intro, order=order,
        )

    topics_by_slug = {}
    for category_slug, topic_list in TOPICS_BY_CATEGORY.items():
        category = categories_by_slug[category_slug]
        for order, (topic_slug, label) in enumerate(topic_list):
            topics_by_slug[topic_slug] = Topic.objects.create(
                slug=topic_slug, label=label, category=category, order=order,
            )

    for entry in COUNSELLORS:
        counsellor = Counsellor.objects.create(
            slug=entry["slug"],
            name=entry["name"],
            credentials=entry["credentials"],
            photo_placeholder=entry["photo_placeholder"],
            location=entry["location"],
            languages=entry["languages"],
            modes=entry["modes"],
            intro=entry["intro"],
            bio=entry["bio"],
            modalities=entry["modalities"],
            fee_note=entry["fee_note"],
        )

        hour_blocks = []
        for weekday, windows in entry["working_hours"].items():
            for start_str, end_str in windows:
                hour_blocks.append(CounsellorWorkingHours(
                    counsellor=counsellor,
                    weekday=weekday,
                    start_time=_time(start_str),
                    end_time=_time(end_str),
                ))
        CounsellorWorkingHours.objects.bulk_create(hour_blocks)

        specialty_links = [
            CounsellorSpecialty(counsellor=counsellor, topic=topics_by_slug[topic_slug], level=level)
            for topic_slug, level in entry["specialties"].items()
        ]
        CounsellorSpecialty.objects.bulk_create(specialty_links)


def reverse_seed_data(apps, schema_editor):
    apps.get_model("core", "Counsellor").objects.all().delete()
    apps.get_model("core", "Topic").objects.all().delete()
    apps.get_model("core", "ServiceCategory").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_servicecategory_counsellor_topic_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed_data),
    ]

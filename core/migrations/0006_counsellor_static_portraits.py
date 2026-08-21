# Move counsellor portraits from MEDIA ImageField uploads to static files.
# Files live at static/images/counsellors/{cards,thumbs}/<slug>.webp.

from django.db import migrations, models


PORTRAITS = {
    "divya-shri": "images/counsellors/cards/divya-shri.webp",
    "jayalakshmi-esakki": "images/counsellors/cards/jayalakshmi-esakki.webp",
    "rakshena": "images/counsellors/cards/rakshena.webp",
    "shaffran": "images/counsellors/cards/shaffran.webp",
    "thara": "images/counsellors/cards/thara.webp",
    "yasotha-natarajan": "images/counsellors/cards/yasotha-natarajan.webp",
}

FACE_FALLBACKS = {
    "aadhithya-m": "images/face_1.avif",
    "divya-shri": "images/face_2.avif",
    "jayalakshmi-esakki": "images/face_3.avif",
    "rakshena": "images/face_4.avif",
    "shaffran": "images/face_5.avif",
    "thara": "images/face_6.avif",
    "yasotha-natarajan": "images/face_7.avif",
}


def point_at_static_portraits(apps, schema_editor):
    Counsellor = apps.get_model("core", "Counsellor")
    for row in Counsellor.objects.all():
        path = PORTRAITS.get(row.slug) or FACE_FALLBACKS.get(row.slug)
        if path:
            row.photo_placeholder = path
            row.save(update_fields=["photo_placeholder"])


def restore_face_placeholders(apps, schema_editor):
    Counsellor = apps.get_model("core", "Counsellor")
    for row in Counsellor.objects.all():
        path = FACE_FALLBACKS.get(row.slug)
        if path:
            row.photo_placeholder = path
            row.save(update_fields=["photo_placeholder"])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_counsellor_photo_placeholder_avif"),
    ]

    operations = [
        migrations.RunPython(point_at_static_portraits, restore_face_placeholders),
        migrations.RemoveField(
            model_name="counsellor",
            name="photo",
        ),
        migrations.AlterField(
            model_name="counsellor",
            name="photo_placeholder",
            field=models.CharField(
                blank=True,
                default="images/face_1.avif",
                help_text="Static path, e.g. images/counsellors/cards/thara.webp",
                max_length=200,
            ),
        ),
    ]

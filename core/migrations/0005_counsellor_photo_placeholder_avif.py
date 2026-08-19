# Generated manually: point placeholders at the AVIF files on disk.

from django.db import migrations, models


def png_placeholders_to_avif(apps, schema_editor):
    Counsellor = apps.get_model("core", "Counsellor")
    for row in Counsellor.objects.all():
        path = row.photo_placeholder or ""
        if path.endswith(".png") and path.startswith("images/face_"):
            row.photo_placeholder = f"{path[:-4]}.avif"
            row.save(update_fields=["photo_placeholder"])


def avif_placeholders_to_png(apps, schema_editor):
    Counsellor = apps.get_model("core", "Counsellor")
    for row in Counsellor.objects.all():
        path = row.photo_placeholder or ""
        if path.endswith(".avif") and path.startswith("images/face_"):
            row.photo_placeholder = f"{path[:-5]}.png"
            row.save(update_fields=["photo_placeholder"])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_counsellor_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="counsellor",
            name="photo_placeholder",
            field=models.CharField(blank=True, default="images/face_1.avif", max_length=200),
        ),
        migrations.RunPython(png_placeholders_to_avif, avif_placeholders_to_png),
    ]

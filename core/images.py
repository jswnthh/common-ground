"""Resize counsellor headshots on upload so list views never download a
full-resolution JPEG. Variants live beside the original:

    counsellors/{name}.jpg          original, capped at ORIGINAL_MAX
    counsellors/thumbs/{stem}.webp  112px (lists, booking, teaser)
    counsellors/cards/{stem}.webp   600px (directory / detail)
"""

from io import BytesIO
from pathlib import Path

from django.core.files.base import ContentFile
from PIL import Image, ImageOps

ORIGINAL_MAX = 800
THUMB_SIZE = 112
CARD_SIZE = 600
WEBP_QUALITY = 82
JPEG_QUALITY = 85


def thumb_name(photo_name):
    return f"counsellors/thumbs/{Path(photo_name).stem}.webp"


def card_name(photo_name):
    return f"counsellors/cards/{Path(photo_name).stem}.webp"


def _open_rgb(file_obj):
    image = Image.open(file_obj)
    image = ImageOps.exif_transpose(image)
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    elif image.mode != "RGB":
        image = image.convert("RGB")
    return image


def _webp_bytes(image):
    buf = BytesIO()
    image.save(buf, format="WEBP", quality=WEBP_QUALITY, method=6)
    return buf.getvalue()


def _jpeg_bytes(image):
    buf = BytesIO()
    image.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
    return buf.getvalue()


def _fitted(image, max_edge):
    fitted = image.copy()
    fitted.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
    return fitted


def _replace(storage, name, content):
    if storage.exists(name):
        storage.delete(name)
    storage.save(name, content)


def write_variants(counsellor, *, cap_original=False):
    """Write thumb/card WebPs. Optionally cap the stored original at ORIGINAL_MAX.

    Safe to call repeatedly; overwrites the derivative files.
    """
    if not counsellor.photo:
        return

    storage = counsellor.photo.storage
    with counsellor.photo.open("rb") as fh:
        image = _open_rgb(fh)

    if cap_original and max(image.size) > ORIGINAL_MAX:
        image = _fitted(image, ORIGINAL_MAX)
        _replace(storage, counsellor.photo.name, ContentFile(_jpeg_bytes(image)))

    _replace(
        storage,
        thumb_name(counsellor.photo.name),
        ContentFile(_webp_bytes(_fitted(image, THUMB_SIZE))),
    )
    _replace(
        storage,
        card_name(counsellor.photo.name),
        ContentFile(_webp_bytes(_fitted(image, CARD_SIZE))),
    )

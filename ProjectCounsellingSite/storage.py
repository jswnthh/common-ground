from whitenoise.storage import CompressedManifestStaticFilesStorage


class QuietWhiteNoiseStorage(CompressedManifestStaticFilesStorage):
    """Hashed static files, but a missing manifest entry is not a 500.

    Django's default ManifestStaticFilesStorage raises ValueError in
    production when {% static %} names a file that was not collected.
    That is the usual cause of a site-wide 500 after DEBUG=False.
    """

    manifest_strict = False

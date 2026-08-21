from whitenoise.storage import CompressedManifestStaticFilesStorage


class QuietWhiteNoiseStorage(CompressedManifestStaticFilesStorage):
    """Hashed static files; a missing file must not 500 the page.

    Django 6's ManifestStaticFilesStorage.stored_name always calls
    hashed_name, which raises if the source is not in STATIC_ROOT.
    WhiteNoise still re-raises that at URL lookup time even when
    manifest_strict is False.
    """

    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            return super().hashed_name(name, content, filename)
        except ValueError:
            return name

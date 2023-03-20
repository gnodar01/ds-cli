from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

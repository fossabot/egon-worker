import importlib.metadata

try:
    __version__ = importlib.metadata.version('asdf')

except importlib.metadata.PackageNotFoundError:
    __version__ = '0.0.0'

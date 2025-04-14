from openalea.spice import *
from importlib.metadata import version, PackageNotFoundError

try:
    from openalea.spice.libspice import *
except ImportError:
    try:
        from openalea.spice.spice import *
    except ImportError:
        import sys

        print("Could not import spice c++ library", file=sys.stderr)


try:
    __version__ = version("openalea.spice")
except PackageNotFoundError:
    # package is not installed
    pass

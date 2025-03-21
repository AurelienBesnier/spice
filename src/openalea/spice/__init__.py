from openalea.spice import *
from .version import __version__

try:
    from openalea.spice.libspice import *
except ImportError:
    try:
        from openalea.spice.spice import *
    except ImportError:
        import sys

        print("Could not import spice c++ library", file=sys.stderr)


__version__ = __version__

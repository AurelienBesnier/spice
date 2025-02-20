from openalea.spice import *

try:
    from openalea.spice.libspice import *
except ImportError:
    try:
        from openalea.spice.spice import *
    except ImportError:
        import sys
        print("Could not import spice c++ library",file=sys.stderr)

from openalea.spice import *

try:
    from openalea.spice.spice import *
except ImportError:
    try:
        from openalea.spice.spice import *
    except ImportError:
        print("Could not import spice c++ library")

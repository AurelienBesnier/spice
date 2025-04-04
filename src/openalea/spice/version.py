#  -*- coding: utf-8 -*-

major = 1
"""(int) Version major component."""

minor = 0
"""(int) Version minor component."""

post = 0
"""(int) Version post or bugfix component."""

__version__ = ".".join([str(s) for s in (major, minor, post)])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from settings.base import *
from settings.prod import *

try:
    from settings.local import *
except ImportError:
    pass
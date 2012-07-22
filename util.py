#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, os

from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging

import settings

handler = SentryHandler(settings.SENTRY_DSN)
setup_logging(handler)

logger = logging.getLogger(os.path.dirname(os.path.realpath(__file__)).split(os.sep)[-1])

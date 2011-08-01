#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# logging singleton class
# 
# @author:     starenka
# @email:      'moc]tod[liamg].T.E[0aknerats'[::-1]
# @version:    1.0
# @since       Nov 24, 2010

import logging,os
from mongolog.handlers import MongoHandler
import settings

class Log(object): 
    dir = os.path.dirname(os.path.realpath(__file__))
    project = dir[dir.rfind('/')+1:]
    log = logging.getLogger(project)
    log.addHandler(MongoHandler.to(db=settings.DB_LOG_NAME,
                                   collection=settings.DB_LOG_COLLECTION,
                                   host=settings.DB_LOG_HOST,
                                   port=settings.DB_LOG_PORT))
    log.setLevel(logging.INFO)

    def __call__(self): return self
    
log = Log().log
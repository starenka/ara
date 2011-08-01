#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# is gd api wrapper

import urllib
import urlgrabber

class IsGd:
    
    API_URL = 'http://is.gd/api.php?longurl='
    
    def shorten(self,uri):
        resp = self._get_uri(self.API_URL+urllib.quote(uri))
        if resp:
            return resp
        else:
            return False
    
    def _get_uri(self,uri,headers = {},timeout = 90.0):
        try:
            ret = urlgrabber.urlread(uri,None,timeout=timeout)
        except Exception, e:
            return False
        return ret



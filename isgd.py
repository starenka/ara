#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# is gd api wrapper

import urllib
import requests

class IsGd:
    
    API_URL = 'http://is.gd/api.php?longurl='
    
    def shorten(self,uri):
        resp = requests.get(self.API_URL+urllib.quote(uri), timeout=30)
        if resp:
            return resp
        else:
            return False
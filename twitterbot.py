#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tweepy wrapper

import tweepy

from isgd import IsGd

class TwitterBot():
    CHARS_MAX_TWEET = 140
    CHARS_MAX_URI = 18 #isgd max uri length
    URL_START = (CHARS_MAX_TWEET-CHARS_MAX_URI-5) #+ ... and spaces
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''

    auth = False
    api = False

    def __init__(self,ctoken,csecret,akey = False,asecret = False):
        self.CONSUMER_KEY = ctoken
        self.CONSUMER_SECRET = csecret
        if akey and asecret: self._auth(akey,asecret)

    def _auth(self,akey,asecret):
        if not self.auth:
            self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY,self.CONSUMER_SECRET)
            self.auth.set_access_token(akey,asecret)
            self.api = tweepy.API(self.auth)

    def get_tokens(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY,self.CONSUMER_SECRET)
        auth_url = auth.get_authorization_url()
        print 'Please authorize: %s'%auth_url
        verifier = raw_input('PIN: ').strip()
        auth.get_access_token(verifier)
        print "ACCESS_KEY = '%s'"%auth.access_token.key
        print "ACCESS_SECRET = '%s'"%auth.access_token.secret                

    def tweet(self,message,akey = False,asecret = False):
        if akey and asecret:
            self._auth(akey,asecret)
        return self.api.update_status(message)            

    def dm(self,to,message,akey = False,asecret = False):
        if akey and asecret:
            self._auth(akey,asecret)
        return self.api.send_direct_message(user=to,text=message)

    def shorten_uri(self,uri):
        return IsGd.shorten(uri)

    def trim_message(self,mess,minus_chars = 0,max_len = 140):
        allowed = max_len-minus_chars
        if len(mess) > allowed:
            return '%s...'%mess[0:allowed-3]
        else:
            return mess
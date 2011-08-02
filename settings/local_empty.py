#!/usr/bin/env python
# -*- coding: utf-8 -*-

#your MongoDB instance settings
DB_LOG_HOST = '127.0.0.1'
DB_LOG_PORT = 27017
DB_LOG_NAME = 'logs'
DB_LOG_COLLECTION = 'ara'

ACCOUNTS = {'meh': {    'key':'meh',
                        'secret':'meh',
                        'triggers': (
                            ('XOXO', #triggering characters f.e "@myaccount XOXO A message to be reposted."
                            '%(mess)s #hi This message includes original reply also with %(user) name',
                             'This will be sent as DM for reply w/ nonexistent trigger.'
                            ),
                        ),
                    },
}

""" Tokens for your app, get yours @ https://dev.twitter.com/apps
    As soon as you have those use "python ara.py -a" to generate key & secret pairs for your accounts."""
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

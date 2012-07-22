#!/usr/bin/env python
# -*- coding: utf-8 -*-

ACCOUNTS = {'meh': {    'key':'meh',
                        'secret':'meh',
                        'triggers': (
                            ('XOXO', #triggering characters f.e "@myaccount XOXO A message to be reposted."
                            '%(mess)s #hi This message includes original reply also with %(user) name',
                            ),
                        ),
                        'not_triggered': 'This will be sent as DM for reply w/ nonexistent trigger.',
                    },
}

""" Tokens for your app, get yours @ https://dev.twitter.com/apps
    As soon as you have those use "python ara.py -a" to generate key & secret pairs for your accounts."""
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

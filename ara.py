#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# twitter repost bot

import sys
from optparse import OptionParser

import settings
from twitterbot import TwitterBot
from util import log as logging

usage = 'Run python ara.py --help to see all options'
oparser = OptionParser(usage)
oparser.add_option('-a','--authenticate',action='store_true',dest='authorize',default = False,\
                  help='get application/account OAuth tokens')
oparser.add_option('-r','--r',action='store',dest='repost',default = False,help='repost replies')
oparser.add_option('-d','--debug',action='store',dest='debug_level',default = 20,help='debug_level')
(options,args) = oparser.parse_args()    

logging.setLevel(int(options.debug_level))

def repost_replies(account_name):
    bf = open('.blacklist_%s'%account_name,'a+')
    blacklist = bf.read().splitlines()
    bf.close()

    rp = open('.reposted_%s'%account_name,'a+')
    reposted = rp.read().splitlines()

    account = settings.ACCOUNTS.get(account_name)

    try:
        logging.info('[%s] Getting last mentions offset'%account_name)
        bot = TwitterBot(settings.CONSUMER_KEY,settings.CONSUMER_SECRET,
                         account['key'],account['secret'])
        mentions = []
        try:
            mentions = bot.api.mentions()
            logging.info('[%s] Got %d mentions'%(account_name,len(mentions)))
        except Exception,e:
            logging.error('[%s] Failed to get mentions. %s'%(account_name,e))

        for mess in reversed(mentions):
            try:
                author = mess.author.screen_name
                if str(author) in blacklist:
                    logging.debug('[%s] Author %s blacklisted. Skipping.'%(account_name,str(author)))
                    continue
                if str(mess.id) in reposted:
                    logging.debug('[%s] Message #%s already reposted. Skipping.'%(account_name,str(mess.id)))
                    continue

                message = mess.text.split(' ')
                if message[0] != '@%s'%account_name:
                    continue #not a "@reply"

                for trigger in account['triggers']:
                    rp.write('%s\n'%mess.id)
                    if message[1] != trigger[0]:
                        logging.warning('[%s] Bad message format, sending DM to author'%account_name)
                        bot.dm(author,trigger[2])
                        break

                    len_params = {'message':'','user':author}
                    mess_len = len(trigger[1]%len_params)
                    params = {'message':bot.trim_message(' '.join(message[2:]),mess_len),'user':author}
                    message = trigger[1]%params
                    logging.info('[%s] Tweeting message %s'%(account_name,message))
                    bot.tweet(message)
            except Exception,e:
                logging.error('%s'%e)
                continue
    except Exception,e:
        logging.error('%s'%e)
    finally:
        rp.close()

if options.authorize:
    bot = TwitterBot(settings.CONSUMER_KEY,settings.CONSUMER_SECRET)
    bot.get_tokens()
    sys.exit('Bye ;)')

if options.repost:
    for account in options.repost.split(' '):
        repost_replies(account.strip())
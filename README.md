Ara : Dummy Twitter bot for reposting replies
========================================================

Ara allows you to repost replies to your accounts on Twitter. You can define mulitple accounts and run the bot for single one or a few at one time:

    python ara.py -r trafficbot-nyc
    python ara.py -r 'trafficbot-nyc trafficbot-amsterdam trafficbot-prague'

For each and every account there are couple settings to be defined:

    ACCOUNTS = {'trafficbot-prague': {  'key':'yourkeyfrom aray.py -a',
                                        'secret':'yoursecretfrom aray.py -a',
                                        'triggers': (
                                            (   'CRASH',
                                                '!! %s #traffic #prague',
                                                'This will be sent as DM for reply w/ nonexistent trigger.'
                                            ),
                                        ),
                                     },
    }

Pay attention to triggers, please. Take a look on @reply below. The first offset in triger touple eqauls to first word in @reply ("CRASH"). Second defines message format which will be reposted ("CRASH %s #crash" -> "!! Car-tram crash in Vodickova, near Vaclavske namesti. Jammed. #traffic #prague") and the last one is the DM which will be sent to replies without any valid trigger.

    @trafficbot-prague CRASH Car-tram crash in Vodickova, near Vaclavske namesti. Jammed.

You can define as many trigger as you want. One more thing, you can also blacklist some users misusing this app by writing their Twitter username in file called .blacklisted_trafficbot-prague (use your account name). One account on each line.

Setup
-----

To install required libs, use pip:

    pip install -r requirements.pip

You can copy local_empty.py as local.py for local testing, this file will be used as setting file if present. Otherwise prod.py will be used. Bot uses MongoDb for logging. In case you don't have/want to use it, just look at util.py and modify it to suit your needs (maybe just standard python logging?).

Twitter mambo jumbo
-----

Create and setup your app at https://dev.twitter.com/apps, as soon as you have consumer key & secret, use

    python ara.py -a

to get keys & secret pairs for all your account defined in settings (you will need to be logged in as the very account during this operation).

Have fun!

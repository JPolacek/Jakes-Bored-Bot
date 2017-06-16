#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'C_KEY'#keep the quotes, replace C_KEY with your consumer key
CONSUMER_SECRET = 'C_SECRET'#keep the quotes, replace C_SECRET with your consumer secret key
ACCESS_KEY = 'A_KEY'#keep the quotes, replace A_KEY with your access token
ACCESS_SECRET = 'A_SECRET'#keep the quotes, replace A_SECRET with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes

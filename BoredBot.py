#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'hfylmh7EkYBQwuXPvymd3lWBq'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'AhAz4KMuyWH58FiNIJ04SMZ0X86Sd5fllreQPvRvrX6tIFTLvt'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '875559505630810112-Vw7X1FmPIx2l4KNlO6GS6PHbhEj8uRy'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'rFCF3DUOfCJaHf7n0Yya9ouOFwNMjv8fIT8m9ArQ4NSei'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes

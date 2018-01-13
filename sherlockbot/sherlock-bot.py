# -*- coding: utf-8 -*-
'''
sherlock holmes cannon words
 pip install python-twitter
 pip install tinydb
'''

import twitter
from tinydb import TinyDB, Query
import random

# db
#dbfile = "/home/baker/bin/sherlockdb.json"
dbfile = "./sherlockdb.json"
db = TinyDB(dbfile)
qry = Query()
# select word
word = db.search(qry['id'] == random.randint(1,len(db.all())))
tweetword = word[0]['source'] + "\n" + word[0]['words']
if len(tweetword) > 140:
	tweetword = tweetword[0:135] + '...'
#print(tweetword)

# twitter api
api = twitter.Api(consumer_key="",
consumer_secret="",
access_token_key="",
access_token_secret="")

status = api.PostUpdate(tweetword)
print(status.text)


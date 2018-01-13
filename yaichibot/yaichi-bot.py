# -*- coding: utf-8 -*-
'''
会津八一 歌う ボット
 pip install python-twitter
 pip install tinydb
'''

import twitter
from tinydb import TinyDB, Query
import random

# db
dbfile = "/home/baker/bin/yaichidb.json"
db = TinyDB(dbfile)
qry = Query()
# select song
song = db.search(qry['id'] == random.randint(1,len(db.all())))
tweetsong = song[0]['comment'] + ".\n" + song[0]['song'] + "\n" + '(' + song[0]['source'] + ')'
#print(tweetsong)

# twitter api

api = twitter.Api(consumer_key="",
consumer_secret="",
access_token_key="",
access_token_secret="")

status = api.PostUpdate(tweetsong)
#print(status.text)


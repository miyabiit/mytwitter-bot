# -*- coding: utf-8 -*-
'''
csv to tinydb
'''

import random
import csv
from tinydb import TinyDB, Query

#file = './test.csv'
file = './docs/aidu_yaichi.csv'
db = TinyDB('yaichidb.json')
db.purge()

with open(file, 'r', encoding = 'utf-8') as f:
	reader = csv.reader(f)
	id = 0
	for row in reader:
		if row == []:
			continue 
		id += 1
		db.insert({'id': id, 'song': row[0], 'source': row[1], 'comment': row[2]})

f.close()

#print(db.all())
print(len(db.all()))
qry = Query()
print(db.search(qry['id'] == random.randint(1,len(db.all()))))
# print(db.all())


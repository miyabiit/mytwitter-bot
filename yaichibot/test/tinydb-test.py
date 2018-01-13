# -*- coding: utf-8 -*-

"""
TinyDB の練習
http://esu-ko.hatenablog.com/entry/2016/03/01/Python%E3%81%A7mongo%E3%82%84json%E3%81%AE%E4%BB%A3%E3%82%8F%E3%82%8A%E3%81%ABtinydb%E3%82%92%E4%BD%BF%E3%81%86

* 辞書データを使う

pip install tinydb
"""

from tinydb import TinyDB, Query
db = TinyDB('testdb.json')

### table ( not must )

table = db.table ('new-t')
table.insert({"data":"value"})

print('テーブル内容全表示',table.all())
print('データは、全てなくなる',db.purge_tables())

### query

db.insert({'type': 'apple','count': 7})
db.insert({'type': 'peach','count': 3})
db.insert({'type': 'pine','count': 12})

print('全レコード表示',db.all())

qry = Query()
print('検索結果:',db.search(qry['type']=='apple'))

db.update({'type':'banana'},qry['type'] == 'pine')
print(db.all())
db.remove(qry['type'] == 'apple')
print(db.all())

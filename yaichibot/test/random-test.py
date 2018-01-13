# -*- coding: utf-8 -*-

'''
random ライブラリの利用
'''

import random

# 0.0 - 1.0 範囲のフロート値
print(random.random())

# 範囲指定のフロート値
print(random.uniform(15,30))

# 範囲指定のint値
print(random.randint(15,30))

# 引数からの一つの要素
print(random.choice('abcdef'))

# リスト要素をシャッフルする
# python3 でrangeはイテレータオブジェクトを返す
sample_list = [i for i in range(1,10,2)]
print(sample_list)
random.shuffle(sample_list)
print(sample_list)


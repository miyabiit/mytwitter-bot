# -*- coding: utf-8 -*-
'''
csv import test
'''

import csv

#file = 'docs/aidu_yaichi.csv'
file = 'test.csv'

# windows cp932 trouble
with open(file, 'r') as f:
	reader = csv.reader(f, delimiter='\t')
	
	for row in reader:
		print(row)

f.close()

# 一行毎、文字列で出力すると 全角スペースが文字化けしない
f = open(file,'r', encoding="utf-8")
line = f.readline()

while line:
	line = f.readline()
	print(line)

f.close()

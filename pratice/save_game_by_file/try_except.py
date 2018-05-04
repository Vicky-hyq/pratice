#!/usr/bin/python
# coding:utf-8

'''
try:
	a =1/0
except:
	import traceback
	traceback.print_exc()
'''

import re

t = '你好吗，我很好！'
m = re.findall(ur'你好',t.decode('utf8'))
if m:
	print m[0].encode('utf8')
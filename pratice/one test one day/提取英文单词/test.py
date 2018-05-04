#!/usr/bin/python
# -*-coding:utf-8 -*-

#从一串信息中提取信息点可以通过正则表达式
import re
f = open ('from.txt')
doc = f.read()
f.close()
m =re.findall('[A-z,\']+',doc)
print m
s = '\n'.join(m)
f1 = open('to.txt','w')
f1.write(s)
f1.close()
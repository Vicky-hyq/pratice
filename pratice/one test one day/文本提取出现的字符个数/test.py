#!/usr/bin/python
# -*- coding:utf-8 -*-


import operator
import sys
#从文件中读取字符串
f = open('t.txt','r')
m =f.read()
f.close()
#m = m.decode('utf-8')
#print m
s = {}
b = 0
n = len(m)
print n
i = 0


while i<n:
	if m[i] not in s:
		s[m[i]] = b+1
	else:
		s[m[i]] += 1
	i += 1

print s

#从小到大排序，解法1
sorted_s=sorted(s.items(),key=operator.itemgetter(1))

print sorted_s

#从小到大排序，接法2,这个按照字典的key来排序
z = zip(s.items())
print z
print sorted(z)

#从小到大排序，解法3
l1 = sorted(s.items(),key = lambda v:v[1])
print 'l1是'
print l1

#从大到小排序
l2 = sorted(s.items(),key=lambda v:v[1],reverse=True)
print l2
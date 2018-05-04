#!/usr/bin/python
# -*- coding:utf-8 -*-

s = 0
for i in xrange(1,101):
	s += i
print s 


#reduce()实现求和
def s(x,y):
	return x+y
print reduce(s,xrange(1,5))


sum1 = reduce(lambda x,y:x+y,xrange(1,101))
print sum1
#!/usr/bin/python
# -*- coding:utf-8 -*-

from random import randint

flag = True
times = 0
s = []
m = 4



while flag == True:
	s.append(randint(1,100))
	if (times >= m):
		flag = False
	times += 1
	print s

print s

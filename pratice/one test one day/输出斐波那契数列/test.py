#!/usr/bin/python
# -*- coding:utf-8 -*-


n = input("请输入数列项的数目：")
x = 3
a1=1
a2=1
s = [1,1]
while x <= n:
	a3 = a1+a2
	s.append(a3)
	a1 = a2
	a2 = a3
	x += 1
print s


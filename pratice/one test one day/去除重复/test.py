#!/usr/bin/python
# -*-coding:utf-8 -*-

l1 = [4, 7, 3, 4, 1, 9, 8, 3, 7 ]
l2 = []


for i in l1:
	if i not in l2:
		l2.append(i)

print l2

l2.sort()
print l2


#简单一句代码

l2=sorted(set(l1))
print l2

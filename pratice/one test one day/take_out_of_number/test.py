#!/usr/bin/python
# -*- coding:utf-8 -*-

l = range(1,101)
s = []
for m in l:
	if (m%2 == 0 and m%3 ==0 and m%5==0):
		print ("%d;"%m)
		s.append(m)
print s

#一行代码显示
#join()函数用法将字符并接到序列中
#s = m for m in range(1,101) if (m%2 == 0 and m%3 ==0 and m%5==0)
print ';'.join([str(m) for m in range(1,101) if (m%2==0 and m%3==0 and m%5==0)])
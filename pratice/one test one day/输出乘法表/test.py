#!/usr/bin/python
# -*-coding:utf-8 -*-

'''
i = 1 
for m in range(1,10):
	while (i <= m):
		s = i*m
		print ("%d * %d = %d"%(i,m,s))
		i = i+1
	i = 1
'''

#参考答案更加简洁

for i in range(1,10):
	for j in range(1,i+1):
		print ("%d * %d = %d"%(j,i,j*i))

#!/usr/bin/python
# -*- coding: utf-8 -*-

#自己写的，实在改不动了
'''
n = input('输入一个正整数：')
x = 0
a = "* "
print a
i =2
while x <= n:
	while (x < i):
		s = a+'* '
		a = s
		print s
		x += 1
	i += 1
'''

n = input('输入一个正整数：')
for i in range(1,n+1):
	for j in range(0,n-i):
		print '',     #这一行：输入一个空字符加逗号，起到输出空格的作用
	for j in range(0,i):
		print '*',
	print      #直接print表示换行


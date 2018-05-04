#!/usr/bin/python
# -*-coding:utf-8 -*-

m = float(raw_input("请输入数字m："))
n = float(raw_input("请输入数字n："))
p = float(raw_input("请输入数字p: "))

'''
if (m>=n):
	if (p>=m):
		print p
	else:
		print m
else:
	if (p>=n):
		print p
	else :
		print n
'''

#参考答案更简洁，长路漫漫。。。
max_num = m
if n > max_num:
	max_num=n
if p >max_num:
	max_num=p
print max_num
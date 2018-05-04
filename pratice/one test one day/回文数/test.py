#!/usr/bin/python
# -*-coding:utf-8 -*-

'''
for i in range(1,201):
	m = i**2
	s = str(m)
	l =len(s)
	n = 0
	for j in range(1,l/2):
		if (s[j] != s[l-j]):
			break
		n = j
	if (n == l/2 and s[n] == s[l-n-1]):
		print i
'''

#python中的字符串逆序

for i in range(1,201):
	m = i**2
	s=str(m)
	s1 = s[::-1] #将字符串逆序这个写法
	if s == s1:
		print i
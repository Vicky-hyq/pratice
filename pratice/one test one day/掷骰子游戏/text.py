#!/usr/bin/python
# coding:utf-8

import random

r1 = random.randint(1,7)
r2 = random.randint(1,7)
r3 = random.randint(1,7)

print r1,r2,r3

r = r1+r2+r3
m =100
while True:
	s = input("选择押大小或者数字，押大小输入1，数字输入2：")
	score = input('输入要押的积分，分数范围1-100：')
	while (score > m):
		print '要押积分已超过当前积分%d，重新输入要押的积分,最多不能超过%d'%(m,m)
		score = input('重新输入要押的积分：')

	if r > 10:
		#print '押注范围为：'
		flag = 2
	else:
		flag = 1


	if s==1:
		n = input("输入押注的范围(3~10)输入1，(11~18)输入2：")
		if n==flag:
			m = m+score*2
		else:
			m = m - score
	else:
		p = input("输入押注的数字，数字范围3-18：")
		if p == r:
			m = m+score*10
		else:
			m = m-score
	print m
	if m < 1:
		print '当前积分已不足够抵扣！！！！'
		break





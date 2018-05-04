#!/usr/bin/python
# -*-coding:utf-8 -*-

import math

a = input('输入a的值：')
b = input('输入b的值：')
c = input('输入c的值：')

m = math.pow(b,2)-4*a*c
print m 
n = math.sqrt(m)
a = 2*a
p1 = (-b + n)/a
p2 = (-b -n)/a

print p1
print p2
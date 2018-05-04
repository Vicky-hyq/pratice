#!/usr/bin/python
#-*- coding:utf-8 -*-

list1 = [1,2,3,4,5,6]
list2 = [1,3,5,7,9,11]
list3 = []

for m in list1:
	list3.append(m*2)
print list3

list4 = [m*2 for m in list1]
print list4

#lambda 参数：表达式
#map(函数，序列)，返回结果为列表,序列若为元组，返回仍列表
list5 = map(lambda x:x*2,list1)
print list5

list6 = map(lambda x,y:x+y,list1,list2)
print list6

l = (1,2,3,4,5)
ll = map(lambda x:x**2,l)
print ll

test = map (None,list1)
print test
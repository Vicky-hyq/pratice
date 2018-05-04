#!/usr/bin/python
# -*- coding:utf-8 -*-

import random 

#生成a到b之间的随机整数,包括a和b，且b>=a
m=random.randint(0,10)
print m

#生成0到1之间的随机浮点数，包括0但不包括1
m = random.random()
print m

#生成a和b之间的随机浮点数，与randint不同的是a/b无需是整数，
#也不用考虑大小
m = random.uniform(1.5,3)
print m
n = random.uniform(3,1.5)
print n

#random.choice(seq)
#从序列中选取一个元素，需要是个序列，如元组，list,字符串
m = random.choice('hello')
print m

#random.randrange(start, stop, step)
#生成一个从start到stop（不包含stop）,间隔为step的一个随机数
#这三个值都是整数
m = random.randrange(4)
print  m

#random.sample(population, k)
#从population序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列。
l = ['sdac',1,2,3,'a']
m = []
m = random.sample(l,3)
print m

#random.shuffle(x)
#将序列x中的元素打乱，生成一个新的序列
x = ['sdac',1,2,3,'a']
m = []
m = random.shuffle(x)
print m
#最后一个编译出来有点问题？？？
#!/usr/bin/python
# -*- coding:utf-8 -*-

import pickle

test = ["cnbc",123,True]

#将这个序列存储到文件中
f = open("E:\personal\pratice\data_change_to_text\gest.txt",'w')
pickle.dump(test,f)
f.close()

#从文件中加载这个序列，并以二进制方式呈现
f = open("E:\personal\pratice\data_change_to_text\gest.txt")
m = pickle.load(f)
print m
f.close()
#!/usr/bin/python
# -*- coding:utf-8 -*-

def func(x,y=5,*a,**b):
	print x,y,a,b


func(1)
func(1,2)
func(1,2,3,4)
func(1,2,a=3,b=4)
func(1,2,3,a=4)
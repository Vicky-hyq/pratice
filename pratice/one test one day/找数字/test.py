#!/usr/bin/python
# -*-coding:utf-8 -*-

import re 

t = "aAsmr3idd4bgs7Dlsf9eAF"

m = re.findall("[0-9]",t)
print m
n = []


n1 = ''.join(m)
print n1
#!/usr/bin/python
# -*- coding:utf-8 -*-

import os 
import fnmatch



for root,dirs,files in os.walk('E:\python'):
	for name in files:
		if fnmatch.fnmatch(name,"*.txt"):
			print name 


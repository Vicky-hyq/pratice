#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import fnmatch 

def findfiles(loc):
	l=[]
	for root,dirs,files in os.walk(loc):
#		print files
		for file in files:
			if fnmatch.fnmatch(file,'*.html'):
				print file
				l.append(file)
	return l

if __name__=='__main__':
	findfiles("E:\personal\pratice")

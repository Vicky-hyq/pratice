#!/usr/bin/python
# coding:utf-8

import sys
import os
import fnmatch
import re

def filterFilename(path,text):
	fileList = []
	for root,dirs,files in os.walk(path):
		for file in files:
				if fnmatch.fnmatch(file,text):
					fileList.append(file)
	return fileList


if __name__ == '__main__':
	'''
	if len(sys.argv) < 3:
		print 'Please input like this:'
	elif os.path.exists(sys.argv[1]):
		FileLists = filterFilename(sys.argv[1],'*.txt')
		print FileLists
		list1=[]
		for file in FileLists:
			with open(file) as f:
				content = f.read()
				if len(re.findall(sys.argv[2],content)) > 0:
					list1.append(file)
		print list1
	else:
		print 'path mno exist.'
	'''
	FileLists = filterFilename('E:\personal\pratice','*.txt')
	print FileLists
	list1=[]
	for file in FileLists:
		with open(file) as f:
			content = f.read()
			if len(re.findall('hi',content)) > 0:
				list1.append(file)
		print list1

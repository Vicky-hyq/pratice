#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
test = "site sea sue sweet see case sse ssee loses"
m = re.findall(r"\bs\S*?e\b",test)

if m:
	print m
else:
	print 'not match!'
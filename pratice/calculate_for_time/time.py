#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
start_time = time.time()
print start_time

for m in range(100):
	print m

end_time = time.time()
n = end_time - start_time
print '输出运行时间%f'%n
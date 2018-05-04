#!/usr/bin/python
# -*- coding:utf-8 -*-

import re

test = '(021)88776543,010-55667890,02584453362,0571 66345673'

#匹配上述的电话号码
m = re.findall(r'\(0\d{2}\)\d{7,8}|0\d{2,3}[- ]?\d{7,8}',test)
print m
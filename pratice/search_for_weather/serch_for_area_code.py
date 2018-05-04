#/usr/bin/python
#-*- coding:utf-8 -*-

import urllib2

url1 = "http://m.weather.com.cn/data5/city.xml"
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')
print provinces

url = 'http://m.weather.com.cn/data3/city.xml'
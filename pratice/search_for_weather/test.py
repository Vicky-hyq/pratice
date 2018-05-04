#!/usr/bin/python
# -*- coding:utf-8 -*-

from city import city
import urllib2
import json
'''
web = urllib2.urlopen("https://www.baidu.com")
result = web.read()
print result
'''

#根据字典提供的城市代码查询城市的天气
getCity = raw_input('请输入要查询的城市名称：')
getCode = city[getCity]
if getCode:
	try:
		web = urllib2.urlopen('http://www.weather.com.cn/data/cityinfo/%s.html'%getCode)
		result = web.read()
		print result
		#将读取到的web上的数据转换成字典形式
		data = json.loads(result)
		para = data ['weatherinfo']
		print ('%s\n%s~%s'%(para['weather'],para['temp1'],para['temp2']))
	except:
		print '查询失败'
else:
	print '没有这个城市'


'''
f = open("E:\personal\pratice\search_for_weather\game.html",'w')
f.write(result)
f.close() 
'''

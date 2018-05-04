#!/usr/bin/python
# -*- coding:utf-8 -*-
# coding:utf-8

import sys

stops = '！，。'
stops = stops.decode('utf-8')
print stops

def  getLength(poe):
	situation = [i for i in range(len(poe)) if poe[i] in stops]
	situation.insert(0,-1)
	print situation
	gaps = [situation[i]-situation[i-1] for i in range(1,len(situation))]
	print gaps
	if gaps:
		return max(gaps)
	else:
		return None


def transferPoetry(poe,sentLength):
	NewPoe = []
	tempSent = []
	for i in poe:
		if  i not in stops:
			tempSent.append(i)
			#print tempSent
		elif len(tempSent) < sentLength:
			tempSent.append(i)
			tempSent +=stops[0]*(sentLength-len(tempSent))
			#print tempSent
			NewPoe.append(tempSent)
			#print NewPoe
			tempSent = []
	RealPoe = []
	for i in xrange(sentLength):
		RealPoe.append([NewPoe[x][i] for x in xrange(len(NewPoe))])
	for i in xrange(len(RealPoe)):
		RealPoe[i].reverse()
		RealPoe[i] = '|'.join(RealPoe[i])
	return RealPoe



if __name__ == '__main__':
	poe = raw_input('Please input your poetry:')
	#print type(poe)
	poe = poe.decode('utf-8')
	#poe = poe.decode(sys.stdin.encoding)
	print len((poe))
	#print type (poe)
	sentLength = getLength(poe)
	if sentLength:
		for i in transferPoetry(poe,sentLength):
			print i 
		else:
			print 'no  poetry!!!'
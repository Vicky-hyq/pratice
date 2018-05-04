#!/usr/bin/python
#! -*-coding:utf-8 -*-

'''
class MyProject:
	name = 'Pratice'

	def forPratice(self):
		print '%s,just for fun!'%self.name

t = MyProject()
print t.name
t.forPratice()
'''

class Viehle:
	def  __init__(self,speed):
		self.speed =speed

	def drive(self,distance):
		time = distance/self.speed
		print ("速度为%.2f"%time)

class Bike(Viehle):
	pass

class Car(Viehle):
	def __init__(self,speed,flue):
		Viehle.__init__(self,speed)
		self.flue = flue

	def drive(self,distance):
		Viehle.drive(self,distance)
		total = distance*self.flue
		print ("燃油量为%.2f"%total)

m = Bike(15)
n = Car(100,0.01)
m.drive(200)
n.drive(200)


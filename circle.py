#!/usr/local/bin/python

'''
Get some information about a circle:
- 2D
- Origin
- Radius

- Area

'''

import numpy as np
import sys

class Circle:
	def __init__(self, origin = (0,0), radius = None):
		try:
			self.set_radius(radius)
		except TypeError:
			#print "This circle has no radius"
			self.radius = None

		self.x = origin[0]
		self.y = origin[1]

	def set_radius(self, radius):
		if radius > 0:
			#print "Setting radius as {}".format(radius)
			self.radius = radius
		else:
			#print "Radius {} Invalid.".format(radius)
			raise TypeError("Circles must have a radius")

	def no_radius(self):
		print "There is no radius"
		return None

	def area(self):
		if self.radius == None:
			return self.no_radius()
		return np.pi*(self.radius**2)	

	def circumference(self):
		if self.radius == None:
			return self.no_radius()
		return np.pi*2*self.radius


if __name__ == "__main__":
	c = Circle()
	print c.area()

	print ""
	radius = 5
	c = Circle(radius = 5)
	print c.area()
	print c.circumference()	

	print ""
	c = Circle(origin = (1, 2))
	radius = 88.1
	c.set_radius(radius)
	print c.area()
	print c.circumference()

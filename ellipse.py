#!/usr/local/bin/python
'''
Implement ellipses and circles
'''

import numpy as np 

class Ellipse():
	def __init__(self, theta = 0,  a = 1, b = 1, origin = (0,0)):
		# Default case is a circle
		if a <= 0 or b <=0:
			print "I don't know how to do singularities"
			raise TypeError("a and b must > 0")
		self.a = a
		self.b = b
		self.theta = theta
		self.x = origin[0]
		self.x = origin[1]

	def set_a(self, value):
		if value > 0:
			self.a = value
		else:
			raise TypeError("a must > 0")
	def set_b(self, value):
		if value > 0:
			self.b = value
		else:
			raise TypeError("b must > 0")
	def set_theta(self, value):
		self.theta = value

	def set_origin(self, value):
		self.x = value[0]
		self.y = value[1]

	def area(self):
		return np.pi*self.a*self.b
	
	def parametric(self):
		x = lambda t: self.a * np.cos(t)
		y = lambda t: self.b * np.sin(t)
		return (x,y)

class Circle(Ellipse):
# Circle is the special case of the ellipse
	def __init__(self, radius = 1):
		self.set_a(radius)
		self.set_b(radius)


if __name__ == '__main__':
	e = Ellipse()
	print "Ellipse area: {}".format(e.area())
		
	c = Circle(3)
	print "Circle area {}".format(c.area())


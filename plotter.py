#!/usr/local/bin/python

'''
Use matplotlib to plot some functions.
'''

import matplotlib.pyplot as plt
import numpy as np
from py import ellipse

def one_pi(step = 0.1):
	return np.arange(0, np.pi+step, step)

def two_pi(step = 0.1):
	return np.arange(0, 2*np.pi+step, step)

def draw():
	pass


n = 100
data = np.random.random((5, n))
data[0,] = data[0,]*np.pi
data[3,] = data[3,]*10
data[4,] = data[4,]*10
for index in range(n):
	theta = data[0,index]
	a = data[1,index]
	b = data[2,index]
	x = data[3,index]
	y = data[4,index]
	e = ellipse.Ellipse(theta, a, b, (x,y))
	x,y = e.parametric()

	x = x(two_pi())
	y = y(two_pi())
		
	plt.plot(x,y)
plt.show()
	


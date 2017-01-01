#!/usr/local/bin/python

'''
Use matplotlib to plot some functions.
'''

import matplotlib.pyplot as plt
import numpy as np
from ellipse import *

def ztopi(step = 0.1):
	return np.arange(0, np.pi, step)

def zto2pi(step = 0.1):
	return np.arange(0, 2*np.pi, step)

def draw():
	pass

if __name__ == '__main__':
	e = Ellipse()
	x,y = e.parametric()

	x = x(zto2pi())
	y = y(zto2pi())
	
	plt.plot(x,y)
	plt.show()
	


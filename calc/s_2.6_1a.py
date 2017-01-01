import numpy
from matplotlib import pyplot as plt


# xy + 2x + 3x^2 = 4

def fn(x,y):
	val = x*y + 2*x + 3*(x**2) - 4
	return val


def run():
	x = np.arange(100)
	y = np.arange(100)

	val = fn(x,y)

	# plot
	


if __name__ == "__main__":
	run()	

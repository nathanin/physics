import matplotlib.pyplot as plt
import numpy as np

b=1

# First time
a=raw_input('Enter a key: ...')
if a=='b': #plot with blue color if press 'b'
	plt.plot(np.arange(10),color='b')
	plt.show(block=False)

elif a=='r': #plot with red color if press 'r'
	plt.plot(np.arange(10),color='r')
	plt.show(block=False)


# update
while b:
	a=raw_input('Enter a key: ...')
	
	if a=='b': #plot with blue color if press 'b'
		plt.plot(np.arange(10),color='b')
		plt.draw()
	
	elif a=='r': #plot with red color if press 'r'
		plt.plot(np.arange(10),color='r')
		plt.draw()
	
	elif a=='q':
		b=0	
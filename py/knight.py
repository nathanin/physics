
# http://stackoverflow.com/questions/40945118/python-knights-shortest-path-chessboard-numbered-0-63

import numpy as np


def get_moves(x,y):
	# location in x,y
	# return a binary image with end points =1
	
	long_move = [2,-2] # long move
	short_move = [1,-1] # short move
	direction = [0,1] # 0=x, 1=y ; initial axis.
	
	board = np.zeros(shape=(8,8), dtype = bool)

	# Janky - skip illegal moves as we go.
	for d in direction:

		for d1 in long_move:

			for d2 in short_move:

				board[x_, y_] = True




def get_coordinates(location, board):
# Translate a numbered location to x,y coordinates
	point = board == location
	x, y = np.nonzero(point)
	x = x[0]
	y = y[0]
	return x, y


def get_binary_location(location, board):
	return board == location


def moveset(location):
# Location 


def find_path(start, end):


def generate_board(size):
	board = np.asarray(range(size**2))
	board = board.reshape(size, size)
	return board



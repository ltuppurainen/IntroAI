from math import inf
import copy

board = [
[0,0,0],
[0,0,0],
[0,0,0]
]

def game_over(board):
	for i in range(0,3):
		tot = 0
		for j in range(0,3):
			tot += board[i][j]
		if abs(tot) == 3:
			return(True)
			
	for i in range(0,3):
		tot = 0
		for j in range(0,3):
			tot += board[j][i]
		if abs(tot) == 3:
			return(True)
	
	tot = 0
	for i in range(0,3):
		tot += board[i][i]
		if abs(tot) == 3:
			return(True)
	
	tot = 0
	for i in range(0,3):
		tot += board[i][(2-i)]
		if abs(tot) == 3:
			return(True)
	
	free_squares = False
	for i in range(0,3):
		for j in range(0,3):
			if board[i][j] == 0:
				free_squares = True
				
	if not free_squares:
		return(True)
			
	return(False)

def winner(board):
	for i in range(0,3):
		tot = 0
		for j in range(0,3):
			tot += board[i][j]
		if abs(tot) == 3:
			return(tot/3)
			
	for i in range(0,3):
		tot = 0
		for j in range(0,3):
			tot += board[j][i]
		if abs(tot) == 3:
			return(tot/3)
	
	tot = 0
	for i in range(0,3):
		tot += board[i][i]
		if abs(tot) == 3:
			return(tot/3)
	
	tot = 0
	for i in range(0,3):
		tot += board[i][(2-i)]
		if abs(tot) == 3:
			return(tot/3)
	
	free_squares = False
	for i in range(0,3):
		for j in range(0,3):
			if board[i][j] == 0:
				free_squares = True
				
	if not free_squares:
		return(0)
		
	print("Weird state")


def possible_boards(board, player):
	boards = []
	
	for i in range(0,3):
		for j in range(0,3):
			if board[i][j] == 0:
				new_board = copy.deepcopy(board)
				new_board[i][j] = player
				boards += [new_board]
	
	return boards
	
def max_value(board, alpha, beta):
	#print("max")
	if game_over(board):
		print("returning end state", winner(board))
		return(winner(board))
	v = -inf
	moves = possible_boards(board, -1)
	for b in moves:
		new_v = min_value(b, alpha, beta)
		print(new_v)
		if new_v == None:
			print(b)
		v = max(v, new_v)
		alpha = max(alpha, v)
		if alpha >= beta:
			print("returning v=", v)
			return(v)
	print("weird")
			
def min_value(board, alpha, beta):
	#print("min")
	if game_over(board):
		print("returning end state", winner(board))
		return(winner(board))
	v = inf
	moves = possible_boards(board, 1)
	for b in moves:
		new_v = max_value(b, alpha, beta)
		print(new_v)
		if new_v == None:
			print(b)
		v = min(v, new_v)
		print(v)
		beta = min(beta, v)
		if alpha >= beta:
			print("returning v=", v)
			return(v)
	print("strange", v, new_v, alpha, beta, board, moves)
			
print(max_value(board, -1, 1))
#print(possible_boards(board, -1))
import numpy as np

board = np.zeros((3,3))
print(board)

def mark_square(row,col,player):
    board[row][col] = player

def square_avail(row,col):
    return board[row][col] == 0

def board_full():
    for i in range(3):
        for j in range(3):
            if(board[i][j] == 0):
                return False
    
    return True


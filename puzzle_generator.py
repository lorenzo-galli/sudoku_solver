from board import board
from values import square_num

initial_board = [[]]

print(board)

for i in range(square_num):
    for j in range(square_num):
        if initial_board[i][j] != "":
            board[i][j].text = initial_board[i][j]
            board[i][j].permanent = True

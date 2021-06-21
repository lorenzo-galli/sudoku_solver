from typing import Counter
from board import board
from values import square_num, num_root

# Here we imput a list with tiles and we return a list of values
def get_values(list):
    values = []
    for tile in list:
        values += tile.text
    return values

# We check if the rows are okay and return a boolean 
def rows_sorted():
    for col in board:

        # we use counters for this. counters are like dictionaries
        values = Counter(get_values(col))

        # if the user hasn't input anything we skip this
        if len(values) >= 1:
            if values.most_common(1)[0][1] > 1:
                return False  # if one element is duplicate we immediately return false
    
    # if it loops through all the cols we return true
    return True


# like the rows the only difference is we have to take the first element of each row
def cols_sorted():
    for _ in range(square_num):
        to_val = []

        for col in board:
            to_val.append(col[_])

        # we convert it into values
        values = Counter(get_values(to_val))
        if len(values) >= 1:
            if values.most_common(1)[0][1] > 1:
                return False
    return True

# this turns the rows and cols board to a board divided by squares
def to_checkboard(board):
    partial = []
    squared_board = []
    for col in board:
        if board.index(col) < num_root:
            for i in range(num_root):
                last_i = (i - 1) * num_root
                partial += col[last_i:i * num_root]
        
        elif board.index(col) >= 3 and board.index(col) < 6:
            for i in range(num_root):
                last_i = (i - 1) * num_root
                partial += col[last_i:i * num_root]
        elif board.index(col) >= 6:
            for i in range(num_root):
                last_i = (i - 1) * num_root
                partial += col[last_i:i * num_root]
        squared_board.append(partial)
    return squared_board

# this works like rows_sorted
def bigsqr_sorted():
    squared_board = to_checkboard(board)
    for square in squared_board:
        values = Counter(get_values(square))
        print(values)
        if len(values) >= 1:
            if values.most_common(1)[0][1] > 1:
                return False
    return True




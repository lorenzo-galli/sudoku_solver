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
    row1 = board[0:3]
    row2 = board[3:6]
    row3 = board[6:9]
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col8 = []
    col9 = []
    for col in row1:
        for tile in col:
            if col.index(tile) < num_root:
                col1.append(tile)
            
            elif col.index(tile) >= 3 and col.index(tile) < 6:
                col2.append(tile)
            elif col.index(tile) >= 6:
                col3.append(tile)
    squared_board.append(col1)
    squared_board.append(col2)
    squared_board.append(col3)
    for col in row2:
        for tile in col:
            if col.index(tile) < num_root:
                col4.append(tile)
            
            elif col.index(tile) >= 3 and col.index(tile) < 6:
                col5.append(tile)
            elif col.index(tile) >= 6:
                col6.append(tile)
    squared_board.append(col4)
    squared_board.append(col5)
    squared_board.append(col6)
    for col in row3:
        for tile in col:
            if col.index(tile) < num_root:
                col7.append(tile)
            
            elif col.index(tile) >= 3 and col.index(tile) < 6:
                col8.append(tile)
            elif col.index(tile) >= 6:
                col9.append(tile)
    squared_board.append(col7)
    squared_board.append(col8)
    squared_board.append(col9)
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

to_checkboard(board)


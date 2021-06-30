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
    is_okay = True
    for col in board:

        # we use counters for this. counters are like dictionaries
        values = Counter(get_values(col))

        # if the user hasn't input anything we skip this
        if len(values) >= 1:
            if values.most_common(1)[0][1] > 1:
                mark_red(values, col)
                is_okay = False

    # if it loops through all the cols we return true
    return is_okay


# like the rows the only difference is we have to take the first element of each row
def cols_sorted():
    is_okay = True
    for _ in range(square_num):
        to_val = []

        for col in board:
            to_val.append(col[_])

        # we convert it into values
            values = Counter(get_values(to_val))
            if len(values) >= 1:
                if values.most_common(1)[0][1] > 1:
                    mark_red(values, to_val)
                    is_okay = False
    return is_okay

# this turns the rows and cols board to a board divided by squares
def to_checkboard(board):
    squared_board = []
    for i in range(1, num_root + 1):
        i_prev = (i - 1) * num_root
        row = board[i_prev:i * num_root]
        col1 = []
        col2 = []
        col3 = []
        for col in row:
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
    return squared_board

def mark_red(values, array):
    for tile in array:
        if tile.text == values.most_common(1)[0][0]:
            tile.is_wrong()


# this works like rows_sorted
def bigsqr_sorted():
    is_okay = True
    squared_board = to_checkboard(board)
    for square in squared_board:
        values = Counter(get_values(square))

        if len(values) >= 1:
            if values.most_common(1)[0][1] > 1:
                mark_red(values, square)
                is_okay = False
    return is_okay

to_checkboard(board)


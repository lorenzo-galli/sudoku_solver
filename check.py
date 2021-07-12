from typing import Counter
from board import board
from values import square_num, num_root, right_sum

# Here we imput a list with tiles and we return a list of values
def get_values(list):
    values = []
    for tile in list:
        values += tile.text
    return values

# We check if the rows are okay and return a boolean 
def rows_sorted():
    unique = True
    correct_sum = True
    for row in board:

        # we use counters for this. counters are like dictionaries
        values = Counter(get_values(row))

        # here we check if the sum is correct
        sum = 0

        # we iterate through the values adding them to the tot sum
        for tile in values:
                sum += int(tile)
                
        # if the sum is correct we can change the tile color to green 
        if sum == right_sum:
            for tile in row:
                tile.is_completed()

        # if it's not we return false
        else: 
            correct_sum = False

        # if the user hasn't input anything we skip this
        if len(values) >= 1:

            # we check if the most common element is repeated more than once
            if values.most_common(1)[0][1] > 1:
                # we mark the tile to red and we return false
                mark_red(values, row)
                unique = False
                
    # if the sum is correct and the values are unique we return completed 
    if correct_sum and unique:
        return 'COMPLETED'

    # if the row is just unique we return No error
    elif unique and not correct_sum:
        return 'No error'
    
    else: 
        return 'ERROR'


# like the rows the only difference is we have to take the first element of each row
def cols_sorted():
    unique = True
    correct_sum = True
    for _ in range(square_num):
        col = []

        for row in board:
            col.append(row[_])
        values = Counter(get_values(col))

        sum = 0

        for tile in values:
                sum += int(tile)
                
        if sum == right_sum:
            for tile in col:
                tile.is_completed()
        else: 
            correct_sum = False

        if len(values) >= 1:
            if values.most_common(1)[0][1] > 1:
                mark_red(values, col)
                unique = False
         
    if correct_sum and unique:
        return 'COMPLETED'
    elif unique and not correct_sum:
        return 'No error'
    else: 
        return 'ERROR'

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
    unique = True
    correct_sum = True
    squared_board = to_checkboard(board)
    for square in squared_board:
        values = Counter(get_values(square))


        sum = 0
        for tile in values:
                sum += int(tile)
                
        if sum == right_sum:
            for tile in square:
                tile.is_completed()
        else: 
            correct_sum = False

    
        if len(values) >= 1:
            if values.most_common(1)[0][1] > 1:
                mark_red(values, square)
                unique = False
        
        
    if correct_sum and unique:
        return 'COMPLETED'
    elif unique and not correct_sum:
        return 'No error'
    else: 
        return 'ERROR'
    

to_checkboard(board)


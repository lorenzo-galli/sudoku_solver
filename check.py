from os import error
from typing import Counter
from board import board, to_checkboard, col_board
from values import square_num, right_sum


# Here we imput a list with tiles and we return a list of values
def get_values(list):
    values = []
    for tile in list:
        values += tile.text
    return values


# this is a function that checks if the values are correct and if the cells are unique
def check(values, array, green):
    unique = True
    correct_sum = True
    # here we check if the sum is correct
    sum = 0

    # we iterate through the values adding them to the tot sum
    for tile in values:
            sum += int(tile)
            
    # if the sum is correct we can change the tile color to green
    if sum == right_sum:
        if green != False:
            for tile in array:
                tile.is_completed()

    # if it's not we return false
    else: 
        correct_sum = False

    # if the user hasn't input anything we skip this
    if len(values) >= 1:

        # we check if the most common element is repeated more than once
        if values.most_common(1)[0][1] > 1:
            # we mark the tile if the user wants to to red and we return false
            if green:
                mark_red(values, array)
            unique = False

    return unique, correct_sum


# We check if the cols are okay and return a boolean 
def cols_sorted(green):
    correct_sum = True
    unique = True
    for col in board:

        # we use counters for this. counters are like dictionaries
        values = Counter(get_values(col))
        loc_unique, loc_correct_sum = check(values, col, green)
        if unique:
            unique = loc_unique
        if correct_sum:
            correct_sum = loc_correct_sum

    # if the sum is correct and the values are unique we return completed 
    if correct_sum and unique:
        return 'COMPLETED'

    # if the row is just unique we return No error
    elif unique and not correct_sum:
        return 'No error'
    
    else: 
        return 'ERROR'


# like the cols the only difference is we have to take the first element of each col
def rows_sorted(green):
    unique = True
    correct_sum = True
    for row in col_board:
        values = Counter(get_values(row))
        loc_unique, loc_correct_sum = check(values, row, green)
        if unique:
            unique = loc_unique
        if correct_sum:
            correct_sum = loc_correct_sum
         
    if correct_sum and unique:
        return 'COMPLETED'
    elif unique and not correct_sum:
        return 'No error'
    else: 
        return 'ERROR'


# we find the wrong cells and we mark them red 
def mark_red(values, array):
    for tile in array:
        if tile.text == values.most_common(1)[0][0]:
            tile.is_wrong()


# this works like cols_sorted
def bigsqr_sorted(green):
    unique = True
    correct_sum = True
    squared_board = to_checkboard(board)
    for square in squared_board:
        values = Counter(get_values(square))
        loc_unique, loc_correct_sum = check(values, square, green)
        if unique:
            unique = loc_unique
        if correct_sum:
            correct_sum = loc_correct_sum
        
    if correct_sum and unique:
        return 'COMPLETED'
    elif unique and not correct_sum:
        return 'No error'
    else: 
        return 'ERROR'
    

# this is just a shortcut to run the functions
def check_all(green):
    cols_sorted(green)
    rows_sorted(green)
    bigsqr_sorted(green)
    col = cols_sorted(green)
    row = rows_sorted(green)
    sqr = bigsqr_sorted(green)
    if col == 'COMPLETED' and row == 'COMPLETED' and sqr == 'COMPLETED':
        return 'COMPLETED'
    elif col == 'ERROR' or row == 'ERROR' or sqr == 'ERROR':
        return 'ERROR'
    else:
        return 'No error'
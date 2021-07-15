from board import board
from values import square_num, num_root
from check import to_checkboard



# Given an array of tiles it finds the text and adds to an array
def fetch_change(array):
    pre_existing = []
    for tile in array:
        if tile.text != '':
            pre_existing += tile.text
    return pre_existing


# Given an array it updates the possible values for each tile
def update_possible(array, changed_tile = None):

    # if a changed tile is given it doesn't call the fetch_change function and updates the other
    if changed_tile != None:
        for tile in array:
            possible = tile.possible

            # permanent tiles already have a well-established value so we can't remove anything
            if not tile.permanent and changed_tile != '':
                try:
                    possible.remove(changed_tile.text)
                except ValueError as e:
                    pass
            tile.possible = possible

    # if a changed tile isn't given we call the fetch_change function
    else: 
        pre_existing = fetch_change(array)
        for tile in array:
            possible = tile.possible

            # permanent tiles already have a well-established value so we can't remove anything
            if not tile.permanent:
                for item in pre_existing:
                    try:
                        possible.remove(item)
                    except ValueError as e:
                        pass
            tile.possible = possible



    # we don't need to return the array because we modified the objects

def update_tile(tile = None):
    for row in board:
        try:
            row_index = row.index(tile)
        except ValueError as e:
            pass
    update_possible(board[row_index], changed_tile=tile)

    for _ in range(square_num):
        col_grid = []

        for row in board:
            col = []
            col.append(row[_])
        col_grid.append(col)

    for col in col_grid:
        try:
            col_index = row.index(tile)
            update_possible(col_grid[col_index], changed_tile=tile)
        except ValueError as e:
            pass
    
    

    squared_board = to_checkboard(board)

    if tile.row < 3:
        if tile.col < 3:
            i = 1
        elif tile.col >= 3 and tile.col < 6:
            i = 2
        if tile.col >= 6:
            i = 3
    elif tile.row >= 3 and tile.row < 6:
        if tile.col < 3:
            i = 4
        elif tile.col >= 3 and tile.col < 6:
            i = 5
        if tile.col >= 6:
            i = 6
    elif tile.row >= 6:
        if tile.col < 3:
            i = 7
        elif tile.col >= 3 and tile.col < 6:
            i = 8
        if tile.col >= 6:
            i = 9

    i -= 1
    update_possible(squared_board[i], changed_tile=tile)
        
def update_all():
    for col in board:
        for tile in col:
            update_tile(tile)

# for col in board:
#     for tile in col:
#         print(tile.possible)



def findCellWithLessCandidates():
    less = 1000000
    tileLess = None
    for col in board: 
        for tile in board:
            if less > len(tile.possible):
                tileLess = tile
    return tileLess



def find_candidates():
    for col in board:
        pass
        


'''
for col in board:
    for tile in col:
        if tile.text == '':
            possibles = tile.possible
            possibles.
'''
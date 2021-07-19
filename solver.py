from draws import draw_board, draw_tiles
from board import swap_rows_cols, col_board
from values import delay, square_num
from check import check_all, to_checkboard
from time import sleep
import pygame


# Given an array it updates the possible values for each tile
def update_possible(array, changed_tile):

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
    # we don't need to return the array because we modified the objects


# we provide a tile and a board and the function updates the correct row, col and square
def update_tile(tile, board):

    # here we update the row the cell is in using its row property
    update_possible(board[tile.row], tile)

    # same thing here with the columns
    col_board = swap_rows_cols(board)
    update_possible(col_board[tile.col], tile)

    # same but with the squares
    squared_board = to_checkboard(board)
    update_possible(squared_board[tile.sqr], tile)


# if we cancel a value from the board we need to re-add it to the possible list
def reAdd_tile(tile):
    pass
        

# this function just updates every tile
def update_all(board):
    for col in board:
        for tile in col:
            update_tile(tile, board)


# this scans all empty cells and returns the one with less possible
def findCellWithLessCandidates():
    tileLess = None
    for col in col_board: 
        for tile in col:
            if tile.text == '':
                if tileLess == None or len(tile.possible) < len(tileLess.possible):
                    tileLess = tile
    return tileLess


# this is the real solving algorithm but doesn't work
def good_solve():

    # we fetch the cell with less candidates
    to_analyze = findCellWithLessCandidates()

    # if it's equal to none it means that there weren't any cell to fill
    if to_analyze == None and check_all():
        print('Puzzle Finished')
        # with open('boards.txt', 'w') as reader:
        #     writer.write(str(board))

        return True

    # if the lenght of the possibilities is equal to 0 we reached a dead point
    elif len(to_analyze.possible) == 0:
        print('Reached the end!') 
        to_analyze.is_wrong()
        return False

    # if none of the two previous cases we can remove the value from the possibilities 
    else:
        to_analyze.text = to_analyze.possible[0]
        to_analyze.checked_values.append(to_analyze.possible[0])
        to_analyze.possible.pop(0)

        # we update the tile possibilities of each tile in the same row, col and sqr
        update_tile(to_analyze, col_board)

        # to make the player see the algorithm in action we update the display and add a delay
        draw_board()
        draw_tiles()
        pygame.display.update()
        sleep(delay)

        # this is a recursive algorithm so we re-call the function
        if not solve():
            if len(to_analyze.possible) == 0:
                to_analyze.possible = to_analyze.checked_values
                return False
            else:
                to_analyze.text = to_analyze.possible[0]
                to_analyze.possible.pop(0)
                solve()
                return True


 
# this is almost a brute force approach
def solve():

    # we fetch the cell with less candidates
    to_analyze = findCellWithLessCandidates()

    # if it's equal to none it means that there weren't any cell to fill
    if to_analyze == None and check_all():
        print('Puzzle Finished')
        return True

    # if the lenght of the possibilities is equal to 0 we reached a dead point
    elif len(to_analyze.possible) == 0:
        print('Reached the end!')
        return False
    
    for i in range(1, square_num + 1):

        # to make the player see the algorithm in action we update the display and add a delay
        draw_board()
        draw_tiles()
        pygame.display.update()
        # sleep(delay)

        to_analyze.text = str(i)
        if check_all(False) == 'No error' or check_all(False) == 'COMPLETED':
            if solve():
                return True
        else:
            to_analyze.text = ''
        
    return False

        
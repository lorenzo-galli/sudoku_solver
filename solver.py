from draws import draw_board, draw_tiles
from board import swap_rows_cols, col_board, board
from values import delay
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
            update_tile(tile, col_board)


# this scans all empty cells and returns the one with less possible
def findCellWithLessCandidates():
    tileLess = None
    for col in col_board: 
        for tile in col:
            if tile.text == '':
                if tileLess == None:
                    tileLess = tile
                elif len(tile.possible) < len(tileLess.possible):
                    tileLess = tile
    try:            
        tileLess.is_solving()
    except AttributeError as e:
        pass
    return tileLess


def solve():
    to_analyze = findCellWithLessCandidates()
    if len(to_analyze.possible) == 0:
        if check_all():
            return 'Done'
        else:
            print('Reached the end!')
    else:
        to_analyze.text = to_analyze.possible[0]
        to_analyze.possible.pop(0)
        print('ok')
        update_tile(to_analyze, col_board)

        draw_board()
        draw_tiles()
        pygame.display.update()
        sleep(delay)
        print(solve())




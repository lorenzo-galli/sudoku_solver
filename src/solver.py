from draws import draw_board, draw_tiles
from board import backboard, swap_rows_cols, col_board, tile
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
 

# this function just updates every tile
def update_all(board):
    for col in board:
        for tile in col:
            tile.fill_possibilities()
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


# this is the solving algorithm. we take two parameters
def solve(is_first = False, all = False):

    # if there is no error we run the algorithm
    if check_all(False) == 'No error':

        # if we choose to count all the solution we need this
        num_of_solutions = 0
        
        # we fetch the cell with less candidates
        to_analyze: tile = findCellWithLessCandidates()
        to_analyze_prev = to_analyze.possible

        # we iterate in the possibilities and we take the first item
        # this is because then we update the cells removing the item
        for i in range(len(to_analyze.possible)):
            try:
                item = to_analyze.possible[0]
            except IndexError as e:
                pass

            # to make the player see the algorithm in action we update the display 
            # and add a delay. if we want all the sol we don't run this
            if not all:
                draw_board()
                draw_tiles()
                pygame.display.update()

            # we assign the item to the text attribute and update the board 
            to_analyze.text = item
            update_tile(to_analyze, col_board)

            # we distinguish between all the solutions and not if we want all the
            # solutions we can return three numbers 0 means no solution found, 1 
            # solution found and unique, 2 more solutions found
            if all:
                output = solve(False, all)
                num_of_solutions += output
                if num_of_solutions > 1:
                    if is_first:
                        return False
                    return 2
                else: 
                    to_analyze.text = ''
                    update_all(col_board)

            else:
                if solve(False) == True:
                    return True
                else:
                    to_analyze.text = ''
                    update_all(col_board)


        # here we return the values making a distinction between all and not all
        # and if it's the first call or not
        if all and num_of_solutions == 1:
            if is_first:
                return True
            return 1
        else:
            to_analyze.possible = to_analyze_prev
            if all and not is_first:
                return 0
            else:
                return False

    # if it's completed we return true or 1
    elif check_all(True) == 'COMPLETED':
        if all:
            return 1
        return True

    # if there is an error false
    else:
        check_all(True)
        return False
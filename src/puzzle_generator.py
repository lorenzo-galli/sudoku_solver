from random import randint
from values import square_num
from json import dumps, loads
from math import floor

boardlink = f'boards/{square_num}x{square_num}.json'


def read_json(file):
    with open(file) as puzzles:
        return loads(puzzles.readline())


def write_to_json(to_write, file):
    opening = read_json(file)
    opening.append(to_write)
    with open(file, 'w') as puzzles:
        puzzles.write(dumps(opening))


list_of_puzzles = read_json(boardlink)
num_of_puzzles = len(list_of_puzzles)
random_num = randint(1, num_of_puzzles-1)

random_num = 2

initial_board = list_of_puzzles[random_num]
empty_board = list_of_puzzles[0]

initial_board = [['', '5', '', '6', '7', '8', '', '', ''], ['6', '7', '', '', '9', '5', '3', '', ''], ['1', '', '8', '3', '', '2', '5', '', '7'], ['8', '', '9', '7', '', '1', '4', '2', ''], ['', '', '', '', '', '3', '7', '9', '1'], ['', '', '', '4', '2', '', '8', '', '6'], ['9', '6', '1', '5', '3', '', '2', '8', ''], ['2', '8', '', '9', '1', '', '6', '5', '3'], ['5', '4', '3', '2', '8', '', '1', '7', '9']]


# Rotates the board clockwise of x degrees
def rotate_board(to_rotate: list, degrees: int, swap_rows_cols):

    rotated, cols = [], []

    # we fill the board with placeholders
    for i in range(square_num):
        for j in range(square_num):
            cols.append("")
        rotated.append(cols)
        cols = []


    # Here we rotate the board based on the degrees
    for jsb in to_rotate:
        for tile in jsb:
            if degrees == 90:
                tile.row = square_num - 1 - tile.row
            elif degrees == 180:
                tile.row = square_num - 1 - tile.row
                tile.col = square_num - 1 - tile.col           
            elif degrees == 270:
                tile.col = square_num - 1 - tile.col
            else:
                print('Use valid degrees')
            rotated[tile.row][tile.col] = tile.text
    
    rotated = swap_rows_cols(rotated)
    
    return rotated


def create_new_puzzles(board, solve):
    solve(True)
    solvable = False

    for i in range(floor(square_num ** 2 / 2)):
        ran_col = randint(0, 8)
        ran_row = randint(0, 8)
        board[ran_col][ran_row].text = ""


    while not solvable:
        ran_col = randint(0, 8)
        ran_row = randint(0, 8)

        board[ran_col][ran_row].text = ""
        solved = solve(True, True)
        if solved:
            solvable = True


def create_new_puzzles(board):
    initial_board = board
    solve(True, False)
    solvable = True

    for i in range(floor(square_num ** 2 / 2)):
        ran_col = randint(0, 8)
        ran_row = randint(0, 8)
        if board[ran_col][ran_row].text == '':
            i -= 1
        board[ran_col][ran_row].text = ''

    print(backboard(board))
    print(solve(True, True))


    for j in range(20):
        # if not solvable:
        #     board = initial_board
        #     print(backboard(board))
        #     return solvable
        #     break
        ran_col = randint(0, 8)
        ran_row = randint(0, 8)
        if board[ran_col][ran_row].text == '':
            j -= 3
        board[ran_col][ran_row].text = ""
        initial_board = board


        # solvable = solve(True, True)
        board = initial_board
        print(backboard(board))
        return solvable
    



print(create_new_puzzles(board))
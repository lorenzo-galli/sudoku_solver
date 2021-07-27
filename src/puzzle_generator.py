from random import randint
from values import square_num
from json import dumps, loads

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

initial_board = list_of_puzzles[random_num]
empty_board = list_of_puzzles[0]


# Rotates the board clockwise of x degrees
def rotate_board(to_rotate: list, degrees: int, swap_rows_cols):

    rotated, cols = [], []

    # we fill the board with placeholders
    for i in range(square_num):
        for j in range(square_num):
            cols.append('')
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


def create_new_puzzles(compl_board: list[list], solve): 
    solvable = True
    while solvable:
        ran_col = randint(0, 8)
        ran_row = randint(0, 8)

        compl_board[ran_col][ran_row].text = ''
        solvable = solve()


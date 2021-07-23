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

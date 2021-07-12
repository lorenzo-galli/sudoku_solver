from board import board
from values import square_num
from check import to_checkboard

for col in board:
    for tile in col:
        for num in range(1, square_num + 1):
            tile.possible += str(num)

def update_possible(array):
    pre_existing = ['6', '3']
    for tile in array:
        if tile.text != '':
            pre_existing += tile.text

    for tile in array:
        possible = tile.possible
        if not tile.permanent:
            for item in pre_existing:
                try:
                    possible.remove(item)
                except ValueError as e:
                    pass

def update_all():
    for row in board:
        update_possible(row)

    for _ in range(square_num):
        col = []

        for row in board:
            col.append(row[_])
        
        update_possible(col)
    
    for square in to_checkboard(board):
        update_possible(square)

update_all()


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
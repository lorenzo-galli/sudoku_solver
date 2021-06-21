from values import *

# This is used to display the screen
pygame.display.set_caption('Sudoku :3')
screen = pygame.display.set_mode((screen_size, screen_size))

# This is the class of the tiles of our 9x9 grid
class tile:
    def __init__(self, row, col, side, total_rows):
        self.row = row
        self.col = col
        self.x = row * side
        self.y = col * side
        self.side = side
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
        self.total_rows = total_rows
        self.text = ''
        self.selected = False
        self.color = back_color

    # Selects the tile
    def select(self):
        self.color = sel_sqr_col
        self.selected = True
        pygame.draw.rect(screen, sel_sqr_col, self.rect, 0)

    # Deselects the tile
    def deselect(self):
        self.color = back_color
        pygame.draw.rect(screen, back_color, self.rect, 0)
        self.selected = False

    def is_wrong(self):
        self.color = red
        pygame.draw.rect(screen, red, self.rect, 0)

# This is to divide the squares 
def make_board():
    board, par_list = [], []
    for col in range(square_num):  # i == y-coordinate
        for row in range(square_num): # j == x-coordinate

            # create a square that take the whole tile and append it to a temporary list
            sqr = tile(row, col, screen_size/square_num, square_num)
            par_list.append(sqr)

        board.append(par_list)  # append the t. list to the final list
        par_list = [] # empty the par list
    return board


board = make_board()


# We return the marked square if any
def get_marked_square():
    for col in board:
        for tile in col:
            if tile.selected == True:
                return tile


def deselect_all_tiles():
    for col in board:
        for tile in col:
            if tile.selected == True:
                tile.deselect()
    return board


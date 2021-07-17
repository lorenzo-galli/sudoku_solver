from values import square_num, num_root, pygame, back_color, sel_sqr_col, green, red, black, screen_size, line_col
from draws import screen
from puzzle_generator import initial_board






# This is the class of the tiles of our 9x9 grid
class tile:
    def __init__(self, row, col, side):
        self.row = col
        self.col = row
        self.sqr = num_root * (self.row // num_root) + (self.col // num_root)
        self.x = row * side
        self.y = col * side
        self.side = side
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
        self.text = ''
        self.selected = False
        self.color = back_color
        self.textColor = line_col
        self.possible = []
        self.permanent = False

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

    def is_completed(self):
        self.color = green
        pygame.draw.rect(screen, green, self.rect, 0)

    def is_permanent(self):
        self.textColor = black
        self.permanent = True
        self.possible = [self.text]


# This is to divide the squares 
def make_board():
    board, par_list = [], []
    for row in range(square_num):  # i == y-coordinate
        for col in range(square_num): # j == x-coordinate

            # create a square that take the whole tile and append it to a temporary list
            sqr = tile(row, col, screen_size/square_num)
            if initial_board[col][row] != "":
                sqr.text = initial_board[col][row]
                sqr.is_permanent()
            if not sqr.permanent:
                for num in range(1, square_num + 1):
                    sqr.possible += str(num)
            par_list.append(sqr)

        board.append(par_list)  # append the t. list to the final list
        par_list = [] # empty the par list
    return board


# We return the marked square if any
def get_marked_square(board):
    for col in board:
        for tile in col:
            if tile.selected == True:
                return tile


def deselect_all_tiles():
    for col in board:
        for tile in col:
            if tile.selected or tile.is_wrong:
                tile.deselect()
    return board


# This is a function mainly used for debugging that prints the board in the terminal
def backboard(board):
    backboard = []
    board = swap_rows_cols(board)
    for row in board:
        col = []
        for tile in row:
            col.append(tile.text)
        backboard.append(col)
    
    for row in backboard:
        print(row)


# Normally the board is an array with other 9 arrays inside of it that represent the rows
# with this function we turn it into an array of columns 
def swap_rows_cols(board):
    col_grid = []
    for _ in range(square_num):
        col = []

        for row in board:
            col.append(row[_])
        col_grid.append(col)
    return col_grid


# this turns the rows and cols board to a board divided by squares
def to_checkboard(board):
    squared_board = []
    for _ in range(square_num):
        col = []
        squared_board.append(col)
    for row in board:
        for tile in row:
            squared_board[tile.sqr].append(tile)
    return squared_board



board = make_board()
col_board = swap_rows_cols(board)
from values import *

initial_board = [
    ['', '', '3', '', '', '', '', '', ''], 
    ['', '', '', '', '', '', '', '7', ''], 
    ['', '', '2', '', '', '', '', '', ''], 
    ['', '', '', '', '', '', '', '', ''], 
    ['', '', '', '', '1', '', '', '9', ''], 
    ['', '', '', '', '', '', '', '', ''], 
    ['', '', '', '', '5', '', '', '', ''], 
    ['', '', '', '', '', '', '4', '', ''], 
    ['', '', '', '', '', '', '', '', ''], 
]

def swap_rows_cols(board):
    col_grid = []
    for _ in range(square_num):
        col = []

        for row in board:
            col.append(row[_])
        col_grid.append(col)
    return col_grid






# This is used to display the screen
pygame.display.set_caption('Sudoku :3')
screen = pygame.display.set_mode((screen_size, screen_size))

# This is the class of the tiles of our 9x9 grid
class tile:
    def __init__(self, row, col, side):
        self.row = col
        self.col = row
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
            if tile.selected or tile.is_wrong:
                tile.deselect()
    return board


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


# this turns the rows and cols board to a board divided by squares
def to_checkboard(board):
    squared_board = []
    for i in range(1, num_root + 1):
        i_prev = (i - 1) * num_root
        row = board[i_prev:i * num_root]
        col1 = []
        col2 = []
        col3 = []
        for col in row:
            for tile in col:
                if col.index(tile) < num_root:
                    col1.append(tile)
                
                elif col.index(tile) >= 3 and col.index(tile) < 6:
                    col2.append(tile)
                elif col.index(tile) >= 6:
                    col3.append(tile)
        squared_board.append(col1)
        squared_board.append(col2)
        squared_board.append(col3)
    return squared_board


col_board = swap_rows_cols(board)
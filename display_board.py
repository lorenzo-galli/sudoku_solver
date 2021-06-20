import pygame
from pygame.constants import *
from pygame.locals import *
from pygame.draw import line
pygame.font.init()

# Colors
sel_sqr_col = '#f2973d'
line_col = '#ffffff'
back_color = '#1d95ad'

# Measurement
size_x = 600
size_y = 600
square_num = 9
sqr_side = size_x/square_num

# Font 
font = pygame.font.Font('freesansbold.ttf', 40)


pygame.init()

# This is used to display the screen
pygame.display.set_caption('Sudoku :3')
screen = pygame.display.set_mode((size_x, size_y))
 

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


# This is to divide the squares 
def make_board():
    board, par_list = [], []
    for col in range(square_num):  # i == y-coordinate
        for row in range(square_num): # j == x-coordinate

            # create a square that take the whole tile and append it to a temporary list
            sqr = tile(row, col, size_x/9, square_num)
            par_list.append(sqr)

        board.append(par_list)  # append the t. list to the final list
        par_list = [] # empty the par list
    return board

board = make_board()

# Draws the numbers and it centers them
def draw_tiles():
    for col in board:
        for tile in col:
            text = font.render(tile.text, True, line_col, tile.color)
            textRect = text.get_rect()
            textRect.center = (tile.x + tile.side/2, tile.y + tile.side/2 + 5)
            screen.blit(text, textRect)


# Draws board and makes line thicker if it's one of the two main lines
def draw_board():
    for i in range(square_num):
        line_div = size_x*i/square_num
        if i % 3 == 0:
            width = 5
        else:
            width = 1
        pygame.draw.line(screen, line_col, (line_div, 0), (line_div, size_y), width)
        pygame.draw.line(screen, line_col, (0, line_div), (size_x, line_div), width)


def deselect_all_tiles():
    for col in board:
        for tile in col:
            if tile.selected == True:
                tile.deselect()
    return board


# We return the marked square if any
def get_marked_square():
    for col in board:
        for tile in col:
            if tile.selected == True:
                return tile


# main loop
def main():
    screen.fill(back_color)

    board = make_board()
    
    running = True
    while running:
        FPS = 60  # Frame rate
        clock = pygame.time.Clock()
        clock.tick(FPS)

        # This captures every event in pygame
        for event in pygame.event.get():
            
            # This is how a player select the square to mark
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                board = deselect_all_tiles()  # if a user pressed with the mouse deselect all
                
                for col in board:  # here we are itering through the rows
                    for tile in col:  # here through the elements
                        
                        if tile.rect.collidepoint(pos):  # if mouse touches tile
                            tile.select()  # we select the tile


            # Here we take the keyboard input and tranform them into outputs
            if event.type == KEYDOWN:
                last_tile = get_marked_square()
                
                try:
                    # We remove the entire array if the backspace is pressed
                    if event.key == K_BACKSPACE:
                        last_tile.text = ''
                    # This allows the player to type one letter max and only num from 1 to 9
                    elif event.key in [K_1, K_2, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9] and len(last_tile.text) == 0:
                        last_tile.text += event.unicode

                    # Here we check if it's a movement key
                    if event.key in [K_DOWN, K_UP, K_RIGHT, K_LEFT, K_s, K_d, K_a, K_w]: 

                        # We get the last tile to understand where to move and we deselect it 
                        last_tile = get_marked_square()
                        board = deselect_all_tiles()

                        
                        # MOVE DOWN
                        if event.key == K_DOWN or event.key == K_s:
                            if last_tile.col > 7:  # if we go too right or down it will throw an index error
                                last_tile.col = -1  # so we need to resect the index to 0
                            tile = board[last_tile.col + 1][last_tile.row]
                            tile.select()

                        # MOVE UP
                        elif event.key == K_UP or event.key == K_w:
                            tile = board[last_tile.col - 1][last_tile.row]
                            tile.select()

                        # MOVE RIGHT
                        elif event.key == K_RIGHT or event.key == K_d:
                            if last_tile.row > 7:
                                last_tile.row = -1
                            tile = board[last_tile.col][last_tile.row + 1]
                            tile.select()

                        # MOVE LEFT 
                        elif event.key == K_LEFT or event.key == K_a:
                            tile = board[last_tile.col][last_tile.row - 1]
                            tile.select()
                    
                # if the user uses keys without having a previous tile it
                # would throw an error so we use except to catch it
                except AttributeError as e:
                    pass


            # This is to quit the game and make sure it doesn't loop forever
            if event.type == pygame.QUIT:
                running = False
        

        # We need to draw our board and our tiles with numbers every frame
        draw_board()
        draw_tiles()

        # This is to make sure the differences are updated and displayed
        pygame.display.update()
    
    pygame.quit()
    quit()

main()

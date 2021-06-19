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
chara = pygame.font.Font('freesansbold.ttf', 40)
text = chara.render('1', True, line_col)


pygame.init()

# This is used to display the screen
pygame.display.set_caption('Sudoku :3')
screen = pygame.display.set_mode((size_x, size_y))
screen.fill(back_color)
 

class tile:
    def __init__(self, row, col, side, total_rows):
        self.row = row
        self.col = col
        self.x = row * side
        self.y = col * side
        self.side = side
        self.rect = (self.x, self.y, self.side, self.side)
        self.total_rows = total_rows
        self.text = text
        self.selected = False

    def select(self):
        pygame.draw.rect(screen, sel_sqr_col, self.rect, 0)
        self.selected = True

    def deselect(self):
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

board = make_board()

# this function checks if a square is selected and deselects it
def deselect_all_tiles():
    for col in board:
        for tile in col:
            if tile.selected == True:
                tile.deselect()
    return board


# main loop
def main():
    running = True
    pressed_key = ''
    board = make_board()
    while running:
        FPS = 60  # Frame rate
        clock = pygame.time.Clock()
        clock.tick(FPS)

        for event in pygame.event.get():
            
            # This is how a player select the square to mark
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                board = deselect_all_tiles()
                for col in board:  # here we are itering through the rows
                    for tile in col:  # here through the elements
                        tile_check = pygame.Rect(tile.rect)
                        if tile_check.collidepoint(pos):
                            tile.select()


            # This allows the player to type one letter max and only num from 1 to 9
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pressed_key = pressed_key[:-1]
                elif event.key in [K_1, K_2, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9] and len(pressed_key) == 0:
                    pressed_key += event.unicode
                print(pressed_key)


            # This is to quit the game and make sure it doesn't loop forever
            if event.type == pygame.QUIT:
                running = False
        
        draw_board()

        # This is to make sure the differences are updated and displayed
        pygame.display.update()
    pygame.quit()
    quit()

main()

import pygame
from pygame.constants import MOUSEBUTTONDOWN
pygame.font.init()

# Colors
sel_sqr_col = '#000000'
line_col = '#ffffff'
back_color = '#1d95ad'

# Measurement
size_x = 600
size_y = 600
sqr_side = size_x/9

# Font 
chara = pygame.font.Font('freesansbold.ttf', 40)

pygame.init()

# This is used to display the screen
pygame.display.set_caption('Sudoku :3')
screen = pygame.display.set_mode((size_x, size_y))
screen.fill(back_color)

# This is to divide the squares  !! TO DO !!
square_num = 9
board = []
print(board)
par_list = []
for i in range(square_num):  # i == y-coordinate
    for j in range(square_num): # j == x-coordinate
        par_list.append(pygame.Rect(size_x*j/9, size_x*i/9, sqr_side, sqr_side))
    board.append(par_list)
board = [board[-1]]
print(board)

text = chara.render('1', True, line_col)
# txt_surf = font.render(str(), True, font_color)
textRect = text.get_rect(center=(50, 50))
screen.blit(text, textRect)

# Draws board and makes line thicker if it's one of the two main lines
for i in range(0, 10):
    line_div = size_x*i/9
    if i % 3 == 0:
        width = 5
    else:
        width = 1
    pygame.draw.line(screen, line_col, (line_div, 0), (line_div, size_y), width)
    pygame.draw.line(screen, line_col, (0, line_div), (size_x, line_div), width)

# main loop
def main():
    running = True
    while running:
        FPS = 60  # Frame rate
        clock = pygame.time.Clock()
        clock.tick(FPS)
        for event in pygame.event.get():

            # This is how a player select the square to mark
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for square in board:
                    for tile in square:
                        if tile.collidepoint(pos):
                            screen.blit(text, tile)
            
            # This is to quit the game and make sure it doesn't loop forever
            if event.type == pygame.QUIT:
                running = False

        # This is to make sure the differences are updated and displayed
        pygame.display.update()
    pygame.quit()
    quit()

main()

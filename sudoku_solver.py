import pygame
from pygame.constants import MOUSEBUTTONDOWN

# Colors
sel_sqr_col = '#000000'
line_col = '#ffffff'
back_color = '#1d95ad'

# Measurement
size_x = 600
size_y = 600
sqr_side = size_x/9

# Font 
font = pygame.font.Font('freesansbold.ttf', 40)

pygame.init()

# This is used to display the screen
pygame.display.set_caption('Sudoku :3')
screen = pygame.display.set_mode((size_x, size_y))
screen.fill(back_color)

# This is to divide the squares  !! TO DO !!
for i in range(1, 9):
    pass

text = font.render('1', True, line_col)
textRect = text.get_rect()


# Draws board and makes line thicker if it's one of the two main lines
for i in range(1, 9):
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
                screen.blit(text, (20, 20))
            
            # This is to quit the game and make sure it doesn't loop forever
            if event.type == pygame.QUIT:
                running = False

        # This is to make sure the differences are updated and displayed
        pygame.display.update()
    pygame.quit()
    quit()

main()

from board import screen, board, col_board
from values import font, num_root, square_num, screen_size, line_col
import pygame

# Draws the numbers and it centers them
def draw_tiles():
    for col in board:
        for tile in col:
            text = font.render(tile.text, True, tile.textColor, tile.color)
            textRect = text.get_rect()
            textRect.center = (tile.x + tile.side/2, tile.y + tile.side/2 + 5)
            screen.blit(text, textRect)


# Draws board and makes line thicker if it's one of the two main lines
def draw_board():
    for i in range(square_num):
        line_div = screen_size*i/square_num
        if i % num_root == 0:
            width = 5
        else:
            width = 1
        pygame.draw.line(screen, line_col, (line_div, 0), (line_div, screen_size), width)
        pygame.draw.line(screen, line_col, (0, line_div), (screen_size, line_div), width)


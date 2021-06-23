from math import sqrt
import pygame

pygame.font.init()

# Colors
sel_sqr_col = '#f2973d'
line_col = '#ffffff'
back_color = '#1d95ad'
red = '#de4e31'

# Measurement
screen_size = 600
square_num = 9
num_root = int(sqrt(square_num))
sqr_side = screen_size/square_num

# Font 
font = pygame.font.Font('freesansbold.ttf', int(sqr_side*3/5))

# Frame rate
FPS = 60  

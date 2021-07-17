from math import sqrt
import pygame

pygame.font.init()

# Colors
sel_sqr_col = '#f2973d'
line_col = '#ffffff'
back_color = '#1d95ad'
red = '#ad1d1d'
green = '#33ad1d'
black = '#000000'
yellow = '#ad931d'

# Measurement
screen_size = 600
square_num = 9
num_root = int(sqrt(square_num))
sqr_side = screen_size/square_num
right_sum = int((square_num * (square_num+1))/2)

# Font 
font = pygame.font.Font('freesansbold.ttf', int(sqr_side*3/5))

# Frame rate & delay
FPS = 60  
delay = 0.015

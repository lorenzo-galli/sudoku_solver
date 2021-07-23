from math import sqrt
import pygame

pygame.font.init()

# This are the default values
square_num = 9
screen_size = 650


# We ask the player if they wants to change the settings
setting = input('Do you want change settings before starting the game?  (s for settings, any other key to play) \n')
if setting.upper() == 'S':
    quit = False


# If they says yes we ask them what to modify
while not quit:
    print(f'\nSETTINGS\n-------------------\nSize of the board: {square_num} x {square_num}\nSize of the window: {screen_size} x {screen_size}\n')
    modify = input('What do you want to modify (board/window/nothing)\n')

    # to change the board and make sure to catch exceptions
    if modify.lower() == 'board' or modify.lower() == 'b':
        ok = False
        while not ok:
            try: 
                square_num = int(input("Which size of the grid do you want (ex. 9x9, 16x16 ecc...)? \n"))
                if int(sqrt(square_num) + 0.5) ** 2 == square_num:
                    ok = True
                else:
                    print('You need to enter a perfect square smaller than 37 (4, 9, 16 ecc...) \n')
            except ValueError as e:
                print('You need to enter a perfect square(4, 9, 16 ecc...) \n')

    # to change the window size and catch exceptions
    elif modify.lower() == 'window' or modify.lower() == 'w':
        ok = False
        while not ok:
            try:
                screen_size = int(input("Which size of the grid do you want (ex. 600, 650 ecc...)? \n"))
                if screen_size <= 1000:
                    ok = True
                else:
                    print('You need to enter a number smaller than 1001\n')

            except ValueError as e:
                print('You need to enter a number smaller than 1001\n')

    # to quit the setting panel and start the game
    elif modify.lower() == 'nothing' or modify.lower() == 'n':
        quit = True


# Colors
sel_sqr_col = '#f2973d'
line_col = '#ffffff'
back_color = '#1d95ad'
red = '#ad1d1d'
green = '#33ad1d'
black = '#000000'


# Measurement
num_root = int(sqrt(square_num))
sqr_side = screen_size/square_num
right_sum = int((square_num * (square_num+1))/2)

# Font 
font = pygame.font.Font('freesansbold.ttf', int(sqr_side*3/5))

# Frame rate & delay
FPS = 60  
delay = 0

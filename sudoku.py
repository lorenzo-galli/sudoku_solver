import pygame
from draws import draw_tiles, draw_board
from board import make_board, get_marked_square, col_board, deselect_all_tiles, screen
from values import back_color, FPS, square_num
from check import rows_sorted, cols_sorted, bigsqr_sorted
from solver import findCellWithLessCandidates, solve, update_all, update_tile
from pygame.constants import *

# main loop
def main():
    screen.fill(back_color)

    board = make_board()
    update_all(col_board)
    
    running = True
    while running:
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

                            # TO REMOVE
                            print(tile.possible)
                            print(tile.checked_values)
                            findCellWithLessCandidates()


            # Here we take the keyboard input and tranform them into outputs
            if event.type == KEYDOWN:
                last_tile = get_marked_square(board)
                
                try:
                    if not last_tile.permanent:
                        # We remove the entire array if the backspace is pressed
                        if event.key == K_BACKSPACE:
                            last_tile.text = ''

                        # This allows the player to type one letter max and only num from 1 to 9
                        elif event.key in [K_1, K_2, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9] and len(last_tile.text) < len(str(square_num)):
                            if int(last_tile.text + event.unicode) <= square_num:
                                last_tile.text += event.unicode
                            else:
                                last_tile.text = str(square_num)
                            update_tile(last_tile, col_board)


                    # This checks if rows, cols and squares are okay
                    if event.key == K_c:
                        board = deselect_all_tiles()
                        print('Squares: ' + bigsqr_sorted())
                        print('Rows: ' + rows_sorted())
                        print('Cols: ' + cols_sorted())


                    # This solves the puzzle
                    if event.key == K_SPACE:
                        solve()

                    # Here we check if it's a movement key
                    if event.key in [K_DOWN, K_UP, K_RIGHT, K_LEFT, K_s, K_d, K_a, K_w]: 

                        # We get the last tile to understand where to move and we deselect it 
                        board = deselect_all_tiles()

                        
                        # MOVE DOWN
                        if event.key == K_RIGHT or event.key == K_d:
                            if last_tile.col > square_num - 2:  # if we go too right or down it will throw an index error
                                last_tile.col = -1  # so we need to resect the index to 0
                            tile = board[last_tile.col + 1][last_tile.row]
                            tile.select()

                        # MOVE UP
                        elif event.key == K_LEFT or event.key == K_a:
                            tile = board[last_tile.col - 1][last_tile.row]
                            tile.select()

                        # MOVE RIGHT
                        elif event.key == K_DOWN or event.key == K_s:
                            if last_tile.row > square_num - 2:
                                last_tile.row = -1
                            tile = board[last_tile.col][last_tile.row + 1]
                            tile.select()

                        # MOVE LEFT 
                        elif event.key == K_UP or event.key == K_w:
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

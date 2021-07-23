# Sudoku Solver

This is a project I developed to practice my python skills and to test them. This is beginner level program so I know there is a lot of room for improvement and tweaks but it was just made for practice so I'll leave it like this.

For this project was used the pygame library to display the board and pure python to handle the checks and algorithms. I stored puzzles to play in json format.

Hope you'll like it ;)


## Resources
As I've said this was done by me but I've looked up some resources to understand how to tackle the problems.

[This about how to generate the puzzle](https://dlbeer.co.nz/articles/sudoku.html)


## How to play
Just run the [python file](https://github.com/lorenzo-galli/sudoku_solver/blob/main/sudoku.py) with pygame installed. 

To select a tile just click it with the mouse or move the arrow keys / WASD.

To mark a tile just press an **ALLOWED** number (any other number won't be accepted). 

Use the backspace key to delete the number.

Press the **C** key to check your board. Any tile with an error will change its color to red. If you completed a row, column or square it will turn green.

Press the **SPACE** key to make the algorithm solve the puzzle.

Press **R** to restart the board, **E** to have an empty board and **N** to have a new puzzle.

You can also change some setting in the file [values.py](https://github.com/lorenzo-galli/sudoku_solver/blob/main/values.py). 

In the [boards directory](https://github.com/lorenzo-galli/sudoku_solver/tree/main/boards) there are some puzzles for the different number of tiles. If you find other valid puzzles just make a **PULL REQUEST**.


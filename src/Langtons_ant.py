"""
Parameters:
grid - a two dimensional array of 1s and 0s (representing white and black cells respectively)
column - horizontal position of ant
row - ant's vertical position
n - number of iterations
dir - ant's current direction (0 - north, 1 - east, 2 - south, 3 - west), should default to 0
Note: parameters column and row will always be inside the grid, and number of generations n will never be negative.

Output
The state of the grid after n iterations.

Rules
The ant can travel in any of the four cardinal directions at each step it takes. The ant moves according to the rules below:

At a white square (represented with 1), turn 90° right, flip the color of the square, and move forward one unit.
At a black square (0), turn 90° left, flip the color of the square, and move forward one unit.
The grid has no limits and therefore if the ant moves outside the borders, the grid should be expanded with 0s, respectively maintaining the rectangle shape.
"""


def ant(grid, column, row, n, direction = 0):
    return "yep"

def step(pos,facing,direction,next):
    pass

def update_grid(array,row,col):
    if array[row][col]:
        array[row][col] = 0
    else:
        array[row][col] = 1
    return array
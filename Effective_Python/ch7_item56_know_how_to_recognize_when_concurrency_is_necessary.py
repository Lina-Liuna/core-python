# expanding the program in a way that maintains clarity, testability, and efficiency.
# change from single-threaded program to multiple concurrentl lines of execution is difficult.

# Example:  Implement conway's game of life.
# Yuu have a two-dimensional grid of an arbitrary size.
# Each cell in the grid can either be alive or empty.

# Game of life is a computer game. invented by John Conway
# Rules:
# 1. Each cell with one or no neighbors dies, as if by solitude
# 2. Each cell with four or more neighbors dies, as if by overpopulation.
# 3. Each cell with two or three neighbors survives.
# 4. Each cell with three neighbors becomes populated.
import numpy

ALIVE = '*'
EMPTY = '-'

# The game progresses one tick of the clock at a time.
# Every tick, each cell counts how many of its neighboring eight cells are still alive.

# represent the state of each cell with a simple container class.
# the cell container class have methods to get and  set the value of any coordinate.

# Coordinates that are out of bounds should wrap around, making the grid act like an infinite looping space.

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []

        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]


    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        rst_str = ""
        for row in self.rows:
            rst_str += ' '.join(row) + '\n'
        return rst_str

# Create a Grid instance and set its initial state to a classic shpae called a glider:

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)

grid.set(1,4, ALIVE)

grid.set(2,2, ALIVE)
grid.set(2,3, ALIVE)
grid.set(2,4, ALIVE)
print(grid)


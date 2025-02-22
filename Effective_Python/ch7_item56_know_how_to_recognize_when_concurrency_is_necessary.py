# expanding the program in a way that maintains clarity, testability, and efficiency.
# change from single-threaded program to multiple concurrentl lines of execution is difficult.

# Example:  Implement conway's game of life.
# Yuu have a two-dimensional grid of an arbitrary size.
# Each cell in the grid can either be alive or empty.

# Game of life is a computer game. invented by John Conway
# Rules:
# 1. Each cell with one or no neighbors dies, as if by solitude
        # die if a cell has fewer than two neighbors
# 2. Each cell with four or more neighbors dies, as if by overpopulation.
        # die if a cell has more than three neighbors
# 3. Each cell with two or three neighbors survives.
# 4. Each cell with three neighbors becomes populated.
        # become alive if an empty cell has exactly three neighbors
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

# Need a way to retrieve the status of neighboring cells.
# retrieve the status of neighboring cells with a helper function that queries the grid
# returns the count of living neighbors

# Use the simple function for the get parameter instead of passing in a whole Grid instance
# to reduce coupling

def count_neighbors(y, x, get):
    n_ = get(y - 1, x + 0)  # North
    ne = get(y - 1, x + 1)  # Northeast
    e_ = get(y + 0, x + 1)  # East
    se = get(y + 1, x + 1)  # Southeast
    s_ = get(y + 1, x + 0)  # South
    sw = get(y + 1, x - 1)  # southwest
    w_ = get(y + 0, x - 1)  # west
    nw = get(y - 1, x - 1)  # northwest
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


# Game of life is a computer game. invented by John Conway
# Rules:
# 1. Each cell with one or no neighbors dies, as if by solitude
        # die if a cell has fewer than two neighbors
# 2. Each cell with four or more neighbors dies, as if by overpopulation.
        # die if a cell has more than three neighbors
# 3. Each cell with two or three neighbors survives.
# 4. Each cell with three neighbors becomes populated.
        # become alive if an empty cell has exactly three neighbors

def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY   # Die: too few
        elif neighbors > 3:
            return EMPTY    # Die: too many
    else:
        if neighbors == 3:
            return ALIVE
    return state

# a function to connect count_neighbors and game_logic together
# a function used to transitions the state of a cell.
# a function will be called each generation to
#   1. figure out a cell's current state,
#   2. inspect the neighboring cells around it,
#   3. determine what its next state should be.
#   4. update the resulting grid accordingly
#   5. use a function interface for set instead of passing in the Grid instance to make this code more decoupled

def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = game_logic(state, neighbors)
    set(y, x, next_state)


# define a function :
#    1. that progresses the whole grid of cells forward by a single step
#    2. returns a new grid containing the state for the next generation
#    3. call get method on the previous generations's Grid instance
#    4. call set method on the next generation's Grid instance
#        3, 4, together to ensure taht all of the cells move in lockstep
#        use function interfaces for get and set instead of passing Grid instances

def simulate(grid):
    next_grid = Grid(grid.height, grid.width)
    for y in range(grid.height):
        for x in range(grid.width):
            step_cell(y, x, grid.get, next_grid.set)
    return next_grid


for i in range(5):
    grid = simulate(grid)
    print("\n")
    print(grid)

# Problem:
# the above works great for a program that can run in one thread on a single machine,
# if the program's requirements have changed, I need to do some I/O(with a socket) from within the game_logic func
# This might be required if I am trying to build a massively meltiplayer online game where  teh state transitions
# are determined by a combination of the grid state and communication with other players over the internet.

# Solution:
# add blocking I/O directly into the game_logic function.

# Problem again:
# the latency of the I/O required is 100 milliseconds, there are 45 cells in the grid
# each generation will take a minimum 4.5 seconds to evaluate because
# each cell is processed serially in the simulate function.

# Solution:
# do the I/O in parallel so each generation takes roughly 100 milliseconds,

# fan-out:
# The process of spawning a concurrent line of execution for each unit of work is called fan-out

# fan-in:
# waiting for all of those concurrent units of work to finish before moveing on to next phase in a coorinated process
# is called fan-in

# slow down the whole program,

# Things-to-Remember:
# 1. A program often grows to require multiple concurrent lines of execution as its scope and complexity increases

# 2. The most common types of concurrency coordination are fan-out(generating new units of concurrency)
# fan-in(waiting for existing units of concurrency to complete)

# 3. Python has many different ways of achieving fan-out and fan-in

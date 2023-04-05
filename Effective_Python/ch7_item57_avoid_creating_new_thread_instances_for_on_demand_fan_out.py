# Threads are the first tool to do parallel I/O in python
# They have significant downsides when you try to use them for fanning out to many concurrent lines of execution.

# use threads to solve the latency problem caused by doing I/O in the game_logic function.

# Threads require coordination using locks to ensure that assumptions within data structures are maintained properly.

# Conway's game of life
# create a subclass of the Grid class that adds locking behavior

from threading import Lock

ALIVE = "*"
EMPTY = "-"

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

class LockingGrid(Grid):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.lock = Lock()

    def __str__(self):
        with self.lock:
            return super().__str__()

    def get(self,y,x):
        with self.lock:
            return super().get(y,x)

    def set(self, y, x, state):
        with self.lock:
            return super().set(y, x, state)

# fan-out:
# The process of spawning a concurrent line of execution for each unit of work is called fan-out

# fan-in:
# waiting for all of those concurrent units of work to finish before moveing on to next phase in a coorinated process
# is called fan-in

# I can reimplement the simulate function to fan out by creating a thread from each call to step_cell
# The threads will run in parallel and won't have to wait on each other's I/O

# then fan in by waiting for all of the threads to complete before moving on to the next generation:

from threading import Thread

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

def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = game_logic(state, neighbors)
    set(y, x, next_state)


def simulate_threaded(grid):
    next_grid = LockingGrid(grid.height, grid.width)

    threads = []
    for y in range(grid.height):
        for x in range(grid.width):
            args = (y,x,grid.get, next_grid.set)
            thread = Thread(target=step_cell, args=args)
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()
    return next_grid


grid = LockingGrid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

for i in range(5):
    grid = simulate_threaded(grid)
    print(grid)

# Problems:
# 1. The thread instances requires sepcial tools to coordinate with each other safety
# 2. Threads requires a lot of memory - 8MB per executing thread
# 3. starting a thread is costly, and threads have a negative performance impact when they run
# due to context switching between them.
# 4. code hard to debug when something went wrong.

# Solution:
# threads are not the solution if you need to constantly create and finish new concurrent functions
# python provide a better fit: Queue

# Things-to-Remember:
# 1. Threads have many downsides:
    # they're costly to start and run if you need a lot of them,
    # they each require a significant amount of memory
    # they require special tools like Lock instances for coordination

# 2. threads don't provide a built-in way to raise exceptions back in the code that started a thread
    # threads makes difficult to debug.

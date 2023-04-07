# Instead of creating one thread per cell per geneartion of the game of life, I can create a fixed number of
# worker thread upfront and have them do parallelized I/O as needed.

# By creating a fixed number of worker thread upfront and have them do parallelized I/O as needed will
# keep the resource usage under control and eliminate the overhead of frequently starting new threads.

# use two CLosableQueue instances to use for communicating to and from the worker threads that execute the
# game_logic function

from queue import Queue

class ClosableQueue(Queue):
    SENTINEL = object()

    # define a close method that adds a special sentinel item to the queue
    # the sentinel item indicates there will be no more input items after it.
    def close(self):
        self.put(self.SENTINEL)


    # define an iterator for the queue thtat looks for this special object
    # and stop iteration when its found.
    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()

in_queue = ClosableQueue()
out_queue = ClosableQueue()

# start multiple threads that will consume items from the in_queue, process them by calling game_logic, and
# put the results on out_queue
from threading import Thread
ALIVE = "*"
EMPTY = "-"

class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


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

def game_logic_thread(item):
    y, x, state, neighbors = item
    try:
        next_state = game_logic(state, neighbors)
    except Exception as e:
        next_state = e
    return (y, x, next_state)

# Start the threads upfront
threads = []
for _ in range(5):
    thread = StoppableWorker(
        game_logic_thread, in_queue, out_queue)
    thread.start()
    threads.append(thread)

class SimulationError(Exception):
    pass

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

def simulate_pipeline(grid, in_queue, out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y, x)
            neighbors = count_neighbors(y, x, grid.get)
            in_queue.put((y, x, state, neighbors))  # Fan out
    in_queue.join()
    out_queue.close()
    next_grid = Grid(grid.height, grid.width)
    for item in out_queue:                          # Fan in
        y, x, next_state = item
        if isinstance(next_state, Exception):
            raise SimulationError(y, x) from next_state
        next_grid.set(y, x, next_state)
    return next_grid

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

for i in range(5):
    print(grid)
    grid = simulate_pipeline(grid, in_queue, out_queue)



for thread in threads:
    in_queue.close()
for thread in threads:
    thread.join()

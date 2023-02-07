# treading module constructs higher-level threading interfaces on top of the lower level _thread module.

# see also:
# 1. concurrent.futures.ThreadPoolExecutor offers a higher level interface to push tasks
# to a background thread without blocking execution of the calling thread, while still being able to
# retrieve their results when needed.

# 2. queue provides a thread-safe interface for exchanging data between running threads

# asyncio offers an alternative approach to achieving task level concurrency without requiring the use of
# multiple operating system threads.

import threading
import random

# thread-local data
# thread-local data is data whose values are thread specific.

mydata = threading.local
mydata = 4

# The run() method invokes the callable object passed to the objects's constructor as the target argument.
t = threading.Thread(target=print, args=[1])
t.run()

t = threading.Thread(target=print, args=(1,))
t.run()

# Timer Objects
# This class represents an action that should be run only after a certain amount of time has passed.

def eat_breads():
    types_of_breads = list()
    types_of_breads = [
        'white bread',
        'multigrain bread',
        'rye',
        'pretzel',
        'hot dog bread',
        'swiss roll',
        'croissant',
        'hamburger',
        'baguette',
        'donut',
        'bagels',
    ]

    random_choice = random.choices(types_of_breads, k=1)

    print(f'Today\'s morning bread is: {random_choice}')

t = threading.Timer(15, eat_breads)
t.start()



# treading module constructs higher-level threading interfaces on top of the lower level _thread module.

# see also:
# 1. concurrent.futures.ThreadPoolExecutor offers a higher level interface to push tasks
# to a background thread without blocking execution of the calling thread, while still being able to
# retrieve their results when needed.

# 2. queue provides a thread-safe interface for exchanging data between running threads

# asyncio offers an alternative approach to achieving task level concurrency without requiring the use of
# multiple operating system threads.

import threading

# thread-local data
# thread-local data is data whose values are thread specific.

mydata = threading.local
mydata = 4
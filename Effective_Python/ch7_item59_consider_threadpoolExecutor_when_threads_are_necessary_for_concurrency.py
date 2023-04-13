# python include the concurrent.futures built-in module
# concurrent.futures provides the ThreadPoolExecutor class.
# ThreadPoolExecutor combines the best of the Thread and Queue approaches to sloving the parallel I/O problem

# Use ThreadPoolExecutor class in game of life program
# Instead of starting a new thread instance for each Grid square, I can fan out by submitting a function
# to an executor that will be run in a separate thread.
# Wait for the result of all tasks in order to fan in.


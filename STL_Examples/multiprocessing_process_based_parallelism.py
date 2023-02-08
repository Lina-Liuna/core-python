# multiprocessing is a package that supports spawning processes using an API similar to the threading module.
# the multiprocessing package offers both local and remote concurrency.
# effectively side-stepping the global interpreter lock by using subprocesses instead of threads.
# the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.

# pool object offers a convenient means of parallelizing the execution of a function across multiple input values.
# pool object distributing the input data across processes.

# the basic example of data parallelism using pool

import multiprocessing

def f(x):
    return x * x
if __name__ == '__main__':         # must contain this line!!!!
    with multiprocessing.Pool(5) as p:
        print(p.map(f, [1,2,3,4,5,6,7,8,9]))

# multiprocessing supports 3 ways to start a process.
# 1. spawn:
# 2. fork:
# 3. forkserver:

# 1. spawn: inherit limited resources, slow compared to using fork or forkserver
# 2. fork: use os.fork() is identical to the parent process, how to safely forking is problematic
# 3. forkserver: whenever needed, the parent process connects to the server and request that it fork a new process.f
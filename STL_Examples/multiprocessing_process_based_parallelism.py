# multiprocessing is a package that supports spawning processes using an API similar to the threading module.
# the multiprocessing package offers both local and remote concurrency.
# effectively side-stepping the global interpreter lock by using subprocesses instead of threads.
# the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.

# pool object offers a convenient means of parallelizing the execution of a function across multiple input values.
# pool object distributing the input data across processes.

# the basic example of data parallelism using pool

import multiprocessing as mp

def f(x):
    return x * x

def foo(q):
    q.put('hello')

def parallelism_with_pool():
    with mp.Pool(5) as p:
        print(p.map(f, [1,2,3,4,5,6,7,8,9]))

# multiprocessing supports 3 ways to start a process.
# 1. spawn:
# 2. fork:
# 3. forkserver:

# 1. spawn: inherit limited resources, slow compared to using fork or forkserver
# 2. fork: use os.fork() is identical to the parent process, how to safely forking is problematic
# 3. forkserver: whenever needed, the parent process connects to the server and request that it fork a new process.
def use_set_start_method():
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

def use_get_context():
    ctx = mp.get_context('fork')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

if __name__ == '__main__':         # must contain this line!!!!
    # parallelism_with_pool()
    # use_set_start_method()
    use_get_context()




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

def f_q(q):
    q.put([42, None, 'hello'])

def f_pipes(conn):
    conn.send([42, None, 'hello'])
    conn.close()

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


# Exchanging objects between processes
# multiprocessing supports two types of communication channel between processes:
# Queues are thread and process safe.

def exchanging_object_queue():
    q = mp.Queue()
    p = mp.Process(target=f_q, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()

def exchanging_object_pipes():
    parent_conn, child_conn = mp.Pipe()
    p = mp.Process(target=f_pipes, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()



# Synchronization between processes:
# How to use lock to ensure that only one process prints to standard output at a time.

def f_lock(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

 # ERROR: self._semlock = _multiprocessing.SemLock._rebuild(*state) FileNotFoundError: [Errno 2] No such file or directory
def sychronization_lock():
    lock = mp.Lock()

    for num in range(10):
        mp.Process(target=f_lock, args=(lock, num)).start()

# Sharing state between processes
# shared memory:
# Data can be stored in a shared memory map using Value or Array.
def f_shared(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

def sharing_state_shared_memory():
    num = mp.Value('d', 0.0)
    arr = mp.Array('i', range(10))

    p = mp.Process(target=f_shared, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

if __name__ == '__main__':         # must contain this line!!!!
    # parallelism_with_pool()
    # use_set_start_method()
    # use_get_context()
    # exchanging_object_queue()
    # exchanging_object_pipes()
    # sychronization_lock()  # ERROR: self._semlock = _multiprocessing.SemLock._rebuild(*state) FileNotFoundError: [Errno 2] No such file or directory
    sharing_state_shared_memory()




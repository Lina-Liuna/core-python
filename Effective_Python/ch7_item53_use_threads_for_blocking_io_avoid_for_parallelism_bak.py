# The standard implementation of python is called CPython
# CPython runs a python program in two steps;
# 1. parses and compiles the source text into bytecode(8-bit instructions)
# 2. CPython runs the bytecode using a stack-based interpreter.

# bytecode interpreter has state that must be maintained and coherent while the Python
# program executes.

# CPython enforces coherence with a mechanism called the global interpreter lock(GIL)

# GIL:
# Global interpreter lock
# GIL is a mutual-exculsion lock(mutex) that prevents CPython from being affected
# by preemptive multithreading.

# GIL prevent one thread may interrupting another thread interpreter state at an
# unexpected time.

# GIL prevent the interruptions and ensures that every bytecode instruction works correctly
# with CPython implementation and its C-extension modules.

# GIL negative side effect:
# GIL reach for threads to do parallel computation and this may not speed up your python programs.


# Example: I want to do something computationally intensive with Python
# I use a navie number factorization algorithm as a proxy.

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

import time


# numbers = [340284, 909093092, 998993]
numbers = [123, 456, 789]
start = time.time()

for number in numbers:
    list(factorize(number))

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# The above code really took such a long time.

# use multiple threads to do this computation would make sense in other language
# because by using multiple threads could take advantage of all the CPU cores of my computer
# define a python thread for doing the same computation as before:

from threading import Thread


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


# Start a thread for each number to factorize in parallel:
start = time.time()
numbers = [340284, 909093092, 998993]  # takes such a long time will skip it.
numbers = [123, 456, 789]
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# Surprisingly, this takes even longer than running factorize in serial!!!!!

# Why?

# This demonstrates the effect of the GIL(lock contention and scheduling overhead)
# GIL on programs running in the standard CPython interpreter.

# There are ways to get CPython to utilize multiple cores, but they dont' work with
# the standard thread class, and they can require substantial effort

# Given these limitations, why does python support threads at all?
# two reasons why python support threads though it not speedup your program?

# 1. multiple threads make it easy for a program to seem like its doing multiple things at the same time.
# managing the juggling act of simultaneous tasks is difficult to implement yourself.
# With threads, you can leave it to python to run your functions concurrently.

# 2. The second reason Python supports threads is to deal with blocking I/O,
# blocking I/O happens when python does certain types of system calls.
# Blocking I/O:
# 1. reading/writing files
# 2. interacting with networks
# 3. communicating with devices like displays


# Example: I  want to send a signal to a remote-controlled helicopter through a serial port.
# use a slow system  call(select) as a proxy for this activity.

import select
import socket

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)


# running the select system call in serial requires a linearly increasing amount of time:
start = time.time()

for _ in range(5):
    slow_systemcall()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# the problem above is:
# when the slow_systemcall function is running, my program can't make any other progress.
# the program's main thread of execution is blocked on the select system call.

# the solution:
# when you found yourself needing to do blocking I/O and computation simultaneously,
# it's time to consider moving your system calls to threads.

start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# The above parallel code took less time than the serial time.

# Why?
# all the system calls will run in parallel from multiple python threads even though they are limited by the GIL

# The GIL prevents my python code from running in parallel, but it doesn't have an effect on system calls.

# This works because python threads release the GIL just before they make system calls,
# and they reacuire the GIL as soon as the system calls are done.

# there a many other ways to deal with blocking I/O besides using threads, like asyncio built-in module.

# using threads is the simplest way to do blocking I/O in parallel with minimal changes to your program.

# Things-to-Remember:
# 1. Python threads can't run in parallel on multiple CPU cores because of the global interpreter lock(GIL)

# 2. Python threads are still useful despite the GIL because they provide an easy way to do multiple things
# seemingly at the same time.

# 3. Use Python threads to make multiple system calls in parallel.
# This allows you to do blocking I/O at the same time as computation.






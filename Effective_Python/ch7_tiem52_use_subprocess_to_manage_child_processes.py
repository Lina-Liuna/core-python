# Chapter 7: Concurrency and Parallelism

# Concurrency enables a computer to do many different things seemingly at the same time.
    # Concurrency providing the illusion that the program are running simultaneously
    # Within a single program, concurrency is a tool that makes it easier for programmers to solve
    # certain types of problems.
    # concurrent programs enable many distinct paths of execution, including separate streams of I/O
    # To make forward progress in a way that seem to be both simultaneous and independent.

# Parallelism, in contrast, involves actually doing many different things at the same time.
    # multiple CPU Cores can execute multiple programs simultaneously.


# Key difference between Parallelism and Concurrency:
    # Speedup
        # two distinct paths of execution in a program make forward progress in parallel
        # the time it takes to do the total work is cut in half.
        # concurrent programs may run thousands of separate paths of execution seemingly
        # in parallel but provide no speedup for the total work.


# How Python support Concurrency?
    # threads
    # coroutines: enable vast numbers of concurrent functions

# How python support Parallel?
    # system calls
    # subprocesses
    # C extensions

# The thing is:
    # it can be very difficult to make concurrent python code truly run in parallel.

# Python provide battle-hardened libraries for running and managing child processes.
    # built-in module: subprocess


# Example: use the subprocess run convenience function to start a process, read its output,
# and verify that it terminated cleanly

import subprocess

result = subprocess.run(
    ['echo', "Hello spring! "],
    capture_output=True,
    encoding='utf-8')

result.check_returncode()
print(result.stdout)


# what is supprocess's parent process?
    # the python interpreter

# Example: use subprocess.Popen class and poll child process status periodically while python does other work.

proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('python working...')
print('Exist status', proc.poll())

# Example: Decoupling the child process from the parent frees up the parent process to run many child processes
# in parallel
# starting all the child processes together with Popen unfront.

import time

start = time.time()
sleep_procs = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', '1'])
    sleep_procs.append(proc)


# wait for all the child processes to finish their I/O and terminate with the communicate method.
for proc in sleep_procs:
    proc.communicate()

end = time.time()
delta = end - start
print(f'Finished in {delta:.3} seconds')




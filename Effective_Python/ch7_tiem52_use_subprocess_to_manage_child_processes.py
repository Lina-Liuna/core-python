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

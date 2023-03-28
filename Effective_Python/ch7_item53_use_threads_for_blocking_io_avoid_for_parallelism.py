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


numbers = [340284, 909093092, 998993]
start = time.time()

for number in numbers:
    list(factorize(number))

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# The above code really took such a long time.





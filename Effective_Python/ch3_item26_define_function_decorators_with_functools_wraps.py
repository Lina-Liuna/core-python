# decorators that can be applied to functions

# A decorator has the ability to run additional code before and after each call to a function wraps.

# decorators can access and modify input arguments, return values, and raised exceptions.

# decorators can be useful for enforcing sematics, debugging, registering functions, and more.

# Example:
# I want to print the arguments and return value of a function call
# This example is helpful when debugging the stack of nested function calls from a recursive function.
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper

#I can apply this decorator to a function by using the @ symbol:
@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

fibonacci = trace(fibonacci)

fibonacci(4)

# the side effect: the value returned by the decorator - the function that's called above - doesn't think
# it's named fibonacci.
print(fibonacci)

# Why?
# The trace function returns the wrapper defined within its body.
# the wrapper function is what's assigned to the fibonacci name in the containing module because of the decorator.

# This behavior is problematic because it undermines tools that do introspection, such as debuugers.
# help func is useless
help(fibonacci)

# Error:
# import pickle
# print(pickle.dumps(fibonacci))
# Solution:
# USE the wraps helper functions from the functools built-in module
from functools import wraps

def trace2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper

#I can apply this decorator to a function by using the @ symbol:
@trace2
def fibonacci2(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci2(n - 2) + fibonacci2(n - 1))

fibonacci2 = trace2(fibonacci2)

fibonacci2(4)

help(fibonacci2)

import pickle
print(pickle.dumps(fibonacci2))

# Things to Remember
# 1. Decorators in Python are syntax to allow one function to modify another function at runtime.
# 2. Using decorators can cause strange behaviors in tools that do introspection, such as debuggers.
# 3. Use the wraps decorator from the functools built-in module when you define your own decorators to avoid issues.

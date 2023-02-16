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





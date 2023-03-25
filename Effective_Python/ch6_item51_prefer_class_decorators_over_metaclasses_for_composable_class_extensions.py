# Example: I want to decorate all of the methods of a class with a helper that
# prints arguments, return values, and exceptions raised.
# I will define the debugging decorator.

from functools import wraps

def trace_func(func):
    if hasattr(func, 'tracing'):
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            print(f'{func.__name__}({args!r}, {kwargs!r}) ->'
                  f'{result!r}')

        wrapper.tracing = True
        return wrapper



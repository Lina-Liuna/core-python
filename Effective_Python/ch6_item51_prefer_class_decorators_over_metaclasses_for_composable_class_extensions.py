# Example: I want to decorate all of the methods of a class with a helper that
# prints arguments, return values, and exceptions raised.
# I will define the debugging decorator.

from functools import wraps


def trace_func(func):
    if hasattr(func, 'tracing'):  # Only decorate once
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


# apply this decorator to various special methods in the new dict subclass
class TraceDict(dict):
    @trace_func
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @trace_func
    def __setitem__(self, *args, **kwargs):
        return super().__setitem__(*args, **kwargs)

    @trace_func
    def __getitem__(self, *args, **kwargs):
        return super().__getitem__(*args, **kwargs)


# trace_dict = TraceDict({'hi', 1})  # Error
trace_dict = TraceDict([('LinaMe', 2), ('Sat', 8)])
trace_dict['weather'] = 'good'
trace_dict['LinaMe'] = 'hi'




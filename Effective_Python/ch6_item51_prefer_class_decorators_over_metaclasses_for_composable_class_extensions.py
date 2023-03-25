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

# Problem: redefine all of the methods that I wanted to decorate with @trace_func.
# it is a redundant boilerplate that's hard to read and error prone.
# Solution: metaclass automatically decorate all methods of a class.

import types


trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MemberDescriptorType,
    types.ClassMethodDescriptorType
)

class TraceMeta(type):
    def __new__(meta, name, bases, class_dict):
        klass = super().__new__(meta, name, bases, class_dict)

        for key in dir(klass):
            value = getattr(klass, key)
            if isinstance(value, trace_types):
                wrapped = trace_func(value)
                setattr(klass, key, wrapped)
        return klass


# what a annoying part of metaclass is the following declare part:
class TraceDict(dict, metaclass=TraceMeta):
    pass

trace_dict = TraceDict([('LinaMe', 2), ('Sat', 8)])
trace_dict['weather'] = 'good'
trace_dict['LinaMe'] = 'hi'

# class decorators
# to Solve what kind of problem?
# Problem: metaclass instance does not inherit from OtherMeta.

# Use class decorator instead!!!!
# class decorator is similar like function decorator


def my_class_decorator(klass):
    klass.extra_param = 'hello'
    return klass


@my_class_decorator
class MyClass:
    pass


print(MyClass)
print(MyClass.extra_param)


def trace(klass):
    for key in dir(klass):
        value = getattr(klass, key)
        if isinstance(value, trace_types):
            wrapped = trace_func(value)
            setattr(klass, key, wrapped)
    return klass


@trace
class TraceDict(dict):
    pass


trace_dict = TraceDict([('LinaMe', 2), ('Sat', 8)])
trace_dict['weather'] = 'good'
trace_dict['LinaMe'] = 'hi'

# Things-to-Remember:

# 1. A class decorator is a simple function that receives a class instance as a parameter and returns either
# a new class or a modified version of the original class.

# 2. Class decorators are useful when you want to modify every method or attribute of a class with minimal boilerplate

# 3. metaclasses can't be composed together easily, while many class decorators can be used to
# extend the same class without conflicts.

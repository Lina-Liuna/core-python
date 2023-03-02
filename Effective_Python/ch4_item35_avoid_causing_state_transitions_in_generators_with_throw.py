# generator advanced fetures:
# 1. yield from expression
# 2. send method
# 3. throw method for re-raising exception instances within generator functions

# How throw method works?
# The way throw works is simple:
# When the method is called, the next occurrence of a yield expression re-raises the provided
# Exception instance after its output is received instead of continuing normally.

# Example:

class MyError(Exception):
    pass

def yield_iter():
    for i in range(1, 4):
        yield i


def my_generator():
    yield from yield_iter()


it = my_generator()
print(next(it))
print(next(it))
# print(it.throw(MyError('test error')))   # exception without try/except error


# When you call throw, the generator function may catch the injected exception with a standard try/except
# compound statement that surrounds the last yield expression that wass executed.
def yield_iter_try():
    for i in range(1, 4):
        try:
            yield i
        except MyError:
            print('Got MyError')


def my_generator_try_except():
    yield from yield_iter_try()


it = my_generator_try_except()
print(next(it))
print(next(it))
print(it.throw(MyError('test error')))
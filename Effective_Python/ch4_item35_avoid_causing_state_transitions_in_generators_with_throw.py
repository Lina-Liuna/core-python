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

# The try/except functionality provides a two-way communication channel between a generator and its caller
# that can be useful in certain situations.

# Example:
# write a program with a timer that supports sporadic resets.
# implement this behavior by defining a generator that relies on the throw method:


class Reset(Exception):
    pass

# whenever the Reset exception is raised by the yield expression, the counter resets itself to its original period.
def sporadic_reset_timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


# connect this counter reset event to an external input that's polled every second.
# define a run function to drive the timer generator, which injects exceptions with throw to cause resets.

def check_for_reset():
    # Poll for external event
    ...


def announce(remaining):
    print(f'{remaining} ticks remaining')


def run():
    it = sporadic_reset_timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

run()



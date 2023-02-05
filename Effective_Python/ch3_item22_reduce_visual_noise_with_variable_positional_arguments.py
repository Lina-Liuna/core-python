# Accepting a variable number of positional arguments can make a function call clearer and reduce visual noise.
# These positional arguments are often called varargs for short, or star args. *args.

# example: log some debugging information. with a fixed number of arguments, I would need a function that takes a msg
# and a list of values.

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ':'.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('Today is Sunday, time is', [5, 43])
log('Raining outside currently', [])

# problem of above solution:
# pass an empty list when have no values to log is cumbersome and noisy.
# It'd be better to leave out the second argument entirely.
# I can do this in python by prefixing the last positional parameter name with *.
# The first parameter for the log message is required, whereas any number of subsequent positional arguments are optional

def log(message, *values):
    if not values:
        print(message)
    else:
        value_str = ':'.join(str(x) for x in values)
        print(f'{message}: {value_str}')

log('Dairy log: Today is Sunday, time is', [5, 43])
log('Dairy log: Raining outside currently')

# star argus syntax works very similarly to the starred expressions used in unpacking assignment statements.

# If I already have a sequence(list a list) and want to call a variable function like log, I can do this by using
# the * operator.
# pass the * operator in input arguments instruct python to pass items from the sequence as positional arguments to
# the function
log_number = [2,3,5,7]
log('Dairy log: log number', *log_number)

# There are two problems with accepting a variable number of positional arguments.
# 1. these optional positional arguments are always turned into a tuple before they are passed to a function
# this means that if the caller of  a function use the *operator on a generator, it will be iterated until it's exhausted.
# The resulting tuple includes every value from the generator, which could consume a lot of memory and
# cause the program to crash.

def my_generator():
    # for i in range(100000000):  # The truth is it takes a long time but not crash....
    for i in range(1000):
        yield  i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)

# Function that accept the *args are best for situations where you know the number of inputs in argument list will
# be reasonably small.

# *args is ideal for function calls that pass many literals or variable names together, for readability of the code.

# the second issue with *args: you can not add new positional arguments to a function in the future without
# migrating every caller.

# if you try to add a positional argument in the front of the argument list, existing callers will subtly break if
# they are not updated.

def log(sequence, message, *values):
    if not values:
        print(f'{sequence}-{message}')
    else:
        value_str = (':').join(str(x) for x in values)
        print(f'{sequence}-{message}:{value_str}')


log(1, 'hi there')
log('Dairy log: log number', *log_number)
log('good morning',2,5)
# log('Dairy log: Raining outside currently') this not worked!!!!!!!


# How to avoid this:
# 1. use keyword-only arguments when you want to extend functions that accept *args
# item 25: enforce clarity with keyword-only and positional-only arguments
# 2. using type annotations
# item 90: consider static analysis via  typing to obviate bugs.















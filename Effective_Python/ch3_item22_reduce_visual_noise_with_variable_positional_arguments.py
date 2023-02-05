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
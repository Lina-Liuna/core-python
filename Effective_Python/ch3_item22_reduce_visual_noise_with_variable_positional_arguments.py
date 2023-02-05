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
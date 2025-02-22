# Sometimes you need to use a non-static type as a keyword arguments default value.

# Example: I want to print logging messages that are marked with the time of the logged event.
# Example: I want the message include time when the function was called.
import time
import datetime

def log(message, when=datetime.datetime.now()):
    print(f'{when}:{message}')

log('lina liu diary log info')
time.sleep(0.3)
log('lina liu login again')        # time in log message not changed!!!

# Why default key argument value in function call not worked as expected?
# because datetime.now() is executed only a single time: when the function is defined.

# A default argument value is evaluated only once per module load, which usually happens when a program starts up.
# After the module containing this code is loaded, the datetime.now() default argument will never be evaluated again.
def log(message, when=None):
    if when is None:
        when = datetime.datetime.now()
    print(f'{when}: {message}')

log('lina liu diary log info')
time.sleep(0.3)
log('lina liu login again')

# Use None for default argument values is especially important when the arguments are mutable.

# Example : I want to load a value encoded as JSON data, if decoding the data fails, I want an empty dictionary
# to be returned by default.

import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


json_data = decode('{"bad data": "3", "huff": "5"}')
json_data['huff'] = 3

json_bar = decode('{bad again}')
json_bar['beep'] = 1
print(f'json_data={json_data}, json_bar={json_bar}')

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print(f'foo={foo}, bar={bar}')

# The above problem: the dictionary specified for default will be shared by all calls to decode because default argument
# values are evaluated only once.
# So cause the so extremely surprising behavior.

# The fix is to set the keyword argument default value to None and then document the behavior in the function's docstring

def decode(data, default=None):
    """Load JSON data from a string.
    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
"""
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

# Things to remember:
# 1. A default argument value is evaluated only once: during function definition at module load time.
# This can cause odd behaviors for dynamic values like {}, [], or datetime.now()

# 2. Use None as the default value for any keyword argument that has a dynamic value.
# Document the actual default behavior in the functions docstring.

# 3. Using None to represent keyword argument default values also works correctly with type annotations.














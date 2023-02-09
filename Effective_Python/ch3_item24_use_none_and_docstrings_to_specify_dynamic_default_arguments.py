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


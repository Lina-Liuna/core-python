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
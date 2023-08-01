# The sched module defines a class which implements a general purpose event scheduler

import sched, time
s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print('From print_time', time.time(), a)

def print_some_times():
    print(time.time())

    # sched.scheduler.enter(delay, priority, action, arguments=(), kwargs={})
    # scheduler.enter() func: schedule an event for delay more time units.
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5,1,print_time, kwargs={'a':'keyword'})

    # Run all scheduled events.
    s.run()

print_some_times()


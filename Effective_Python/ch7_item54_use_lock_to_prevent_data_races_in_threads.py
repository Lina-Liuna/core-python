# if we already have global interpreter lock(GIL)
# we can forgo using mutual-exclusion locks(mutexes) in the code altogether, right?

# Not truly the case.
# The GIL will not protect you although only one Python thread runs at a time.
# A threads operations on data structures can be interrupted between any two bytecode instructions in
# python interpreter.

# Example: write a program that counts many things in parallel
# like sampling light levels from a whole network of sensors.

# If I want to determine the total number of light samples over time, I can aggregate them with a new class

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset

# Imagine that each sensor has its own worker thread because reading from the sensor requires blocking I/O
# After each sensor measurement, the worker thread increments the counter up to maximum number of desired readings.

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        counter.increment(1)


# Run one worker thread for each sensor in parallel and wait for them all to finsih their readings.
from threading import Thread

how_many = 10 ** 5
counter = Counter()

threads = []
for i in range(5):
    thread = Thread(target=worker,
                    args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f'Counter should be {expected}, got {found}')

# why expected and found not the same?

# In python, the python interpreter enforces fairness between all of the threads
# that are executing to ensure they get roughly equal processing time.

# Python suspends a thread as it's running and rsumes another.
# you don't know exactly when python will suspend your threads.

# The only operation is simple:
# counter.count += 1
# but the bytecode instruction looks like it split three operations:
value = getattr(counter, 'count')
result = value + 1
setattr(counter, 'count', result)

# Solution:
# to prevent data races like these,
# Python includes a robust set of tools in the threading built-in module.
# the simplest and most useful of them is the Lock class, a mutual-exclusion lock(mutex)

from threading import Lock

class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset

counter = LockingCounter()

for i in range(5):
    thread = Thread(target=worker,
                    args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f"Counter should be {expected}, got{found}")


# Things-to-Remember:
# 1. Even though python has a global interpreter lock, you're still responsible for protecting
# against data races between the threads in your programs

# 2. You programs will corrupt their data structures if you allow multiple threads to modify
# the same objects without mutual-exclusion locks(mutex)

# 3. Use the Lock class from the threading built-in module to enforce your programs
# invariants between multiple threads.





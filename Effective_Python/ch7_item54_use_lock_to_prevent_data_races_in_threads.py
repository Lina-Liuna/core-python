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

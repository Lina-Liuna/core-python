# hooks: built-in APIs allows you to customize behavior by passing in function.
# hooks are used by APIs to call back your code while they execute.

# many hooks are just stateless functions with well-defined arguments and return values.
# functions are ideal for hooks because they are earier to describe and simpler to define than classes.

# hooks simple example:
# customize the behavior of the defaultdict class.
# the hook function return the default value that the missing key should have.
# define a hook that logs each time a key is missing and returns 0 for the default value.
import collections


def log_missing():
    print('Key added')
    return 0


current = {'red': 8, 'pink': 70}
increments = [
    ('blue', 20),
    ('orange', 10),
]

result = collections.defaultdict(log_missing, current)
print('before:', (dict(result)))

for key, amount in increments:
    result[key] += amount

print('after:', (dict(result)))



# Problem: supplying functions like log_missing makes APIs easy to build and test
# the default value hook passed to defaultdict to count the total number of keys that were missing.
# define a helper function that uses such a closure as the default value hook:

def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count    # Stateful closure
        added_count += 1
        return 0

    result = collections.defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

current = {'red': 8, 'pink': 70}
increments = [
    ('blue', 20),
    ('orange', 10),
]

result, count = increment_with_report(current, increments)
print(count)


# Improvement: define a small class that encapsulates the state you want to track.
class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = collections.defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount

print(counter.added)

# Problem: until you see the use of CountMissing Class with defaultdict, the class is a mystery

# Solution:
# to clarify this situation, class can define the __call__ special method.
# __call__ allows an objects to be called just like a function.
# __call__ function causes the callable built-in function to return True like a normal function or method.
# All objects that can be executed in this manner are referred to as callables:

class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0
counter = BetterCountMissing()
result = collections.defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
print(counter.added)


# ALl the defaultdict requires a function for the default value hook, choose wisely.

# Things-to-Remember:
# 1. Instead of defining and instantiating classes, you can often simply use functions for simple interfaces between
# components in Python.

# 2. Reference to functions and mothods in Python are first class, meaning they can be used in expressions.

# 3. The __call__ special method enables instances of a class to be called like plain Python functions.

# 4. When you need a function to maintain state, consider defining a class that provide the __call__ method instead of
# defining a stateful closure.



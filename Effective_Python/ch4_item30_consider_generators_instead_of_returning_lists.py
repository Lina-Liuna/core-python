# we often return list of items
# print(len('# we often return list of items'))
# what's the side effect of return list of items?
# There is one line for creating the result list and another for returning it.
# all results to be stored in the list before being returned, for huge inputs, this can cause a program
# to run out of memory and crash.


# A better way to write this function is by using a generator.
# Generators are produced by functions that use yield expressions.
# return a generator can easily be adapted to take inputs of arbitrary length due to its bounded memory requirements.

# Example: I want to find the index of every word in a string.
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

car_words = "steering wheel, clutch, brake, gas pedal, gear level, speedometer, rearview mirror, dashboard"
print(list(index_words_iter(car_words)))

# Example: I define a generator that streams input from a file one line at a time and yields outputs one word at a time
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if offset == ' ':
                yield offset

import os, itertools

with open(os.path.basename(__file__), 'r') as f:
    it = index_file(f)
    res = itertools.islice(it, 0, 5)
    print(list(res))





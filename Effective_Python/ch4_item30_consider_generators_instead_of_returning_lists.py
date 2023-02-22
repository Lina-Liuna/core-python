# we often return list of items
# what's the side effect of return list of items?
# There is one line for creating the result list and another for returning it.

# A better way to write this function is by using a generator.
# Generators are produced by functions that use yield expressions.

# Example: I want to find the index of every word in a string.
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

car_words = "steering wheel, clutch, brake, gas pedal, gear level, speedometer, rearview mirror, dashboard"
print(list(index_words_iter(car_words)))

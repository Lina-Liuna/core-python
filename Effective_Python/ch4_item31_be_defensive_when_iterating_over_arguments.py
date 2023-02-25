# Example: I want to analyze tourism numbers for the U.S. state of Texas,
# the data set is the number of visitors to each city
# I'd like to figure out what percentage of overall tourism each city receives.

# I need a normalization function that sums the inputs to determine the total number of tourists per year
# and then divides each city's individual visitor count by the total to find that city's contribution to the whole.
import itertools
import os


def normalize(numbers):
    total = sum(numbers)
    for value in numbers:
        percent = 100 * value / total
        yield percent


visits = [56, 78, 95]
percentages = normalize(visits)
percentages, percentages_backup = itertools.tee(percentages)
print(list(percentages))
print(sum(list(percentages_backup)))


def write_numbers_to_file(file_path):
    with open(file_path, 'w') as f:
        for i in range(100):
            f.write(str(i))
            f.write('\n')


path = os.getcwd() + 'numbers.txt'
write_numbers_to_file(os.getcwd() + 'numbers.txt')


# read the data from a file that contains every city in all of Texas.
# define a generator to do this because I can reuse the same function later
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits(os.getcwd() + 'numbers.txt')
percentages = normalize(it)
percentages, percentages_backup = itertools.tee(percentages)
print(list(percentages))
print(sum(list(percentages_backup)))


# The iterator produces its results only a single time.
# If you iterate over an iterator or a generator that has already raised a StopIteration exception,
# you won't get any results the second time around.

# How to solve the iterator exhausted problem?
# one way around this is to accept a function that returns a new iterator each time it's called.
#

# the input argument  is an iterator.
def normalize_func(get_iter):
    total = sum(get_iter())     # new iterator
    for value in get_iter():
        percent = 100 * value / total
        yield percent


percentages = normalize_func(lambda: read_visits(path))
percentages, percentages_backup = itertools.tee(percentages)
print(list(percentages))
print(sum(list(percentages_backup)))



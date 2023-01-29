# if you return more than 3 values, especially return values are numeric:
#
# it is all to easy to recorder them accidentally.
# which can cause bugs that are hard to spot later.
# Using a large number of return values is extremely error prone.

#For example:
# Correct:
#minimum, maximum, average, median, count = get_stats(lengths)
# Oops! Median and average swapped:
# minimum, maximum, median, average, count = get_stats(lengths)

# Second, the line that calls the functions and unpacks the values is long.

# To avoid these problems, you should never use more than three variables when unpacking the multiple return values.
# the return values can be three-tuple, two variables and one catch-all starred expression or namedtuple.

def get_avg_ratio(numbers):
    avarage = sum(numbers) / len(numbers)
    scaled = [x / avarage for x in numbers]
    scaled.sort(reverse=True)
    return scaled

number_list = [19, 40, 25, 56, 79, 92, 23]
longest, *middle, shortest = get_avg_ratio(number_list)
print(f'longest: {longest:>4.0%}')
print(f'shortest:{shortest:>4.0%}')


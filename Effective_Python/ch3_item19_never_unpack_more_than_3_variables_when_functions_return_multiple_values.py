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





# This module provides support for maintaining a list in sorted order
# without having to sort the list after each insertion.

# Useful for long lists of items:
# For long lists of items with expensive comparison operations, this can be an improvement over the more common approach.

# Why it called bisect?
# because it uses basic bisection algorithm to do its work.

# NOTES:
# 1. bisection is effective for searching ranges of values.
# but for locating specific values, dictionaries are more performant.

# 2. the insort() functions are O(n) because the lagrithmic search step is dominated by the linear time insertion step

# teeny-tiny-useful:
# bisect() function can be useful for numeric table lookups.
# example: uses bisect() to look up a letter grade for an exam score based on a set of ordered numeric breakpoints:
# 90 and up is 'A', '80 to 89 is B'
import bisect


def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

scores = [55,66,77,88,99]
grades = [grade(score) for score in scores]
print(grades)

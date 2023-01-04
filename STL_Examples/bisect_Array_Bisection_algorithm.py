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
import collections


def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

scores = [55,66,77,88,99]
grades = [grade(score) for score in scores]
print(grades)

# teeny-tiny-useful:
# bisect() and insort() func work with lists of tuples.
# The key argument can serve to extract the field used for ordering records in a table.
import collections
import bisect
import operator
import pprint
Movie = collections.namedtuple('Movie', ('name', 'released', 'director'))
movies = [
    Movie('schindlers List', 1993, 'Steven Spielberg'),
    Movie('Taxi Driver', 1996,'Martin Scorsese'),
    Movie('The Martian',2015,'Ridley Scott'),
    Movie('Ying hung boon sik',1986,'John Woo'),
]

# Find first movie released after 1980
by_year = operator.attrgetter('released')
movies.sort(key=by_year)
print(movies)
#help(bisect.bisect)
#m = movies[bisect.bisect_left(movies, 1988, key=by_year)]


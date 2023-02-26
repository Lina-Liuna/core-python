# The problem with list comprehensions is that they may create new list instance containing one item for each value
# in input sequences.

# create new list instance is fine for small inputs, but for large inputs, this behavior could consume significant
# amounts of memory and cause a program to crash.


# Example: read a file and return the number of characters on each line
# If using list comprehensions and if the file is enormous and perhaps a never-ending network socket, using
# list comprehensions would be problematic.
import os
value = [len(x) for x in open (os.path.basename(__file__))]
print(value)

# Python provide generator expressions.
# what is generator expressions?
# Generator expressions are a generalization of list comprehensions and generators.
# generator expression don't materizalize the whole output sequence when they're run.

# Generator expressions evaluate to an iterator that yields one item at a time from the expression.

# how to create a generator expression?
# Create a generator expression by putting list-comprehension-like syntax between () characters.

it = (len(x) for x in open(os.path.basename(__file__)))
# print(list(it))
print(it)
print(next(it))
print(next(it))

# another powerful outcome of generator expressions is that they can be composed together.
# take the iterator returned by the generator expression above and use it as the input of another generator expression

roots = ((x, x**0.5) for x in it)
print(next(roots))
print(next(roots))

# chaining generators together like above executes very quickly in python.

# when you're looking for a way to compose functionality that's operating on a large stream of input,
# generator expressions are a greate choice.

# The only gotcha is that the itertator returned by generator expressions are stateful, so you must be careful not to
# use these iterators more than once.

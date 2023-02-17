# Comprehensions is extended to functions with generators

# the generator enable a stream of values to be incrementally returned by a function.

# The result of a call to a generator function can be used anywhere an iterator is appropriate.

# Generators can improve performance, reduce memory usage, and increase readability.


# what is list comprehensions?
# the compact syntax for deriving a new list from another sequence or iterable.

a = ['a', 'b', 'c', 'd', 'e']

# suare_a is a list comprehension
square_a = [x*3 for x in a]
print(square_a)
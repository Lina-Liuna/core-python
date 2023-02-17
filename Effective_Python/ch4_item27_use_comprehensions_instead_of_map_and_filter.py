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

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square_a = [x ** 2 for x in a if x % 2 == 0]
print(square_a)

even_square_dict = {x: x**2 for x in a if x % 2 == 0}
print(even_square_dict)

threes_cubed_dict= {x: x**3 for x in a if x % 3 == 0}
print(threes_cubed_dict)

# Things to remember:

# 1. List comprehensions are clearer than the map and filter built-in functions
# because they don’t require lambda expressions

# 2. List comprehensions allow you to easily skip items from the input list,
# a behavior that map doesn’t support without help from filter.

# 3. Dictionaries and sets may also be created using comprehensions.
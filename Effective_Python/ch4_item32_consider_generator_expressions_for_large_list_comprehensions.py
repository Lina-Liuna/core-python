# The problem with list comprehensions is that they may create new list instance containing one item for each value
# in input sequences.

# create new list instance is fine for small inputs, but for large inputs, this behavior could consume significant
# amounts of memory and cause a program to crash.



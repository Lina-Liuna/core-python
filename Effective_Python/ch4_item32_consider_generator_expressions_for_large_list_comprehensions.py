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
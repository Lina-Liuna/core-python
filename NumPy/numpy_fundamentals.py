import numpy as np

# NumPy is the fundamental package for scientific computing in Python.
# It is a python library that provide a multidimensional arrary object, various derived objects
import numpy.random

a1D = np.array([x for x in range(5)])
a2D = np.array([[x,y] for x in range(1, 5, 2) for y in range(2, 6, 2)])
print(a1D)
print(a2D)


a = np.array([127, 128, 129], dtype=np.int8)
print(a)

# 1D array cration functions:
a = np.arange(10)
print(a)
print(a[0])

a = np.arange(2, 10, dtype=float)
print(a)

a = np.arange(2, 3, 0.2)
print(a)

# this linspace include the stop 4. inside the result arrary
a = np.linspace(1., 4., 6)
print(a)

# 2D array creation functions

a = np.eye(3)
print(a)

# np.eye(n, m) defines 2D indentity matrix, the elements where i=j are 1 and the rest are 0
a = np.eye(3, 5)
print(a)

# np.diag define either a square 2D array with given values
a = np.diag([1, 2, 3])
print(a)

a = np.diag([1, 2, 3], 1)
print(a)

a = np.array([[1,2], [3, 4]])
print(a)
a = np.diag(a)
print(a)

a = np.zeros((2, 3))
print(a)

a = np.ones((2, 3))
print(a)

# numpy.random.default_rng(2) create an array filled with random values between 0 and 1
# the seed set to 2 so you can reproduce these pseudorandom numbers
a = numpy.random.default_rng(2).random((2,3))
print(a)

a = numpy.random.default_rng(2). random((2,3,2))
print(a)

a = np.indices((3,3))
print(a)

a = np.arange(1.0, 4.0, 1.0)
b = np.array([2.0, 2.0, 2.0])
print(a * b)

b = 2.0
print(a*b)

print(np.typecodes['All'])
print(np.typecodes['AllFloat'])
print(np.typecodes['AllInteger'])
print(np.typecodes)

# numpy.can_cast() returns True if cast between data types can occur according to the casting rule.

mark = {False: '-', True: 'Y'}
def print_table(ntypes):
    print('X ' + ' '.join(ntypes))
    for row in ntypes:
        print(row, end=' ')
        for col in ntypes:
            print(mark[np.can_cast(row, col)], end= ' ')
        print()

print_table(np.typecodes['All'])





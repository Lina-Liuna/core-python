import numpy as np

# NumPy is the fundamental package for scientific computing in Python.
# It is a python library that provide a multidimensional arrary object, various derived objects

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



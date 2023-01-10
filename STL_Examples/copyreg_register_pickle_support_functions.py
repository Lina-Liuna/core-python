# the copyreg module offers a way to define functions used which pickling specific objects.
# The pickle and copy module use those functions when pickling/copying those objects.

# The copyreg module provides configuration information about object constructors which are not classes.

# How to register a pickle function and how it will be used.
import copyreg, copy, pickle
class C:
    def __init__(self, a):
        self.a = a

def pickle_c(c):
    print('pickling a C instance...')
    return C, (c.a,)

copyreg.pickle(C, pickle_c)
c = C(1)
d = copy.copy(c)
p = pickle.dumps(c)

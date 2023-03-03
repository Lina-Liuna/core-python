# The itertools built-in module contains a large number of functions that are useful for
# organizing and itteracting with iterators

import itertools

# whenever you find yourself dealing with tricky iteration code, it's worthy looking at the itertools
# The following sections describe the most important functions that you should know

# 1. Linking iterators together
    # 1. chain
    # 2. repeat
    # 3. cycle
    # 4. tee
    # 5. zip_longest
# 2. Filtering items from iterator:
    # 1. islice
    # 2. takewhile
    # 3. dropwhile
    # 4. filterfalse
# 3. Producing combinations of items from iterator:
    # 1. accumulate
    # 2. product
    # 3. permutations
    # 4. combinations
    # 5. combinations_with_replacement

# 1. Linking iterators together
# 1. chain : use chain to combine multiple iterators into a single sequential iterator.

class IterGen:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for i in range(self.start, self.end):
            yield i

iter_1 = IterGen(1, 4)
iter_2 = IterGen(4, 8)
iter_3 = IterGen(8, 12)
it = itertools.chain(iter_2, iter_1, iter_3)
print(list(it))

# 2. repeat: Use repeat to output a single value forever, or
# use the second parameter to specify a maximum number of times.
it = itertools.repeat('hello Lina', 5)
print(list(it))

# 3. cycle: use cycle to repeat an iterator's item forever:

it = itertools.cycle(list(iter_1))
result = [next(it) for _ in range(10)]
print(result)


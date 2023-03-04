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

# 2. repeat:
# Use repeat to output a single value forever, or
# use the second parameter to specify a maximum number of times.
it = itertools.repeat('hello Lina', 5)
print(list(it))

# 3. cycle:
# use cycle to repeat an iterator's item forever:

it = itertools.cycle(list(iter_1))
result = [next(it) for _ in range(10)]
print(result)

# 4. tee:
# use tee to split a single iterator into the number of parallel iterators specified by the second parameter
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))

# 5. zip_longest:
# # zip_longest is the variant of the zip built-in function,
# zip_longest return a placeholder value when an iterator is exhausted, which may happen if iterator have
# different lengths:

keys = ['one', 'two', 'three']
values = [1, 2]

normal = list(zip(keys, values))
print(normal)

it = itertools.zip_longest(keys, values, fillvalue='nope')
print(list(it))


# Filtering items from an iterator
# the itertools built-in module include a number of functions for filtering items from an iterator.

# 6. islice:
# use islice to slice an iterator by numerical indexes without copying.
# you can specify the end, start and end, or start, end and step sizes.

values = [x for x in range(1, 11)]
first_five = itertools.islice(values, 5)
print(list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print(list(middle_odds))

# 7. takewhile:
# takewhile returns items from an iterator until a predicate function returns False for an item.
values = [x for x in range(1, 11)]
less_then_seven = lambda x: x < 7

it = itertools.takewhile(less_then_seven, values)
print(list(it))

my_str = 'Once Upon tree treat train triple tractor try trouble trail truck tricky true these them mother'

str_list = my_str.split(' ')
print(str_list)

len_less_than_5 = lambda x: len(x) <= 5
it = itertools.takewhile(len_less_than_5, str_list)
print(list(it))

# 8. dropwhile:
# dropwhile is the opposite of takewhile, skips items from an iterator until the predicate function returns True
# from the first time:
it = itertools.dropwhile(len_less_than_5, str_list)
print(list(it))

# 9. filterfalse
# filterfalse is oppsite of the filter built-in function, returns all items from an iterator where a predicate
# function returns False:

even_len = lambda x: len(x) % 2 == 0
filter_result = filter(even_len, str_list)
print(list(filter_result))

filter_result = filter(len_less_than_5, str_list)
print(list(filter_result))

filter_false_result = itertools.filterfalse(even_len, str_list)
print(list(filter_false_result))

filter_false_result = itertools.filterfalse(len_less_than_5, str_list)
print(list(filter_false_result))


# Producing combinations of items from iterators
# The itertools built-in module includes a number of functions for producing combinations of items from iterators.
# 10. accumulate:
# accumulate folds an item from the iterator into a running value by applying a function that takes two parameters.
sum_accumulate = itertools.accumulate(str_list)
print(list(sum_accumulate))


sum_values = itertools.accumulate(values)
print(list(sum_values))

def sum_modulo_20(first, second):
    output = first + second
    return output % 20

modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print(list(modulo_reduce))

def sum_modulo_20(first, second):
    output = first
    return output % 20

# itertools.accumulate(iterable[, func, *, initial=None])
# If func is supplied, it should be a function of two arguments.
# Elements of the input iterable may be any type that can be accepted as arguments to func.
# (For example, with the default operation of addition, elements may be any addable type including Decimal or Fraction.)
modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print(list(modulo_reduce))

import operator
print(list(itertools.accumulate(values, operator.mul)))
print(list(itertools.accumulate(values, max)))
print(list(itertools.accumulate(values, lambda x, y: x * y * 3.14)))













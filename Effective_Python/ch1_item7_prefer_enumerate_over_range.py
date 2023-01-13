# the range built-in function is useful for loops that iterate over a set of integers
# randint Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

from random import randint

random_bits = 0
for i in range(32):
    if randint(0,1):
        random_bits |= 1 << i

print(random_bits)
print(bin(random_bits))

for i in range(32):
    print(i, 1 << i)

# when you have a data structure to iterate over, like a list of strings,
# you can loop directly over the sequences
flavor_list = ['pineapple', 'mango', 'strawberry', 'vanilla']
for flavor in flavor_list:
    print(f'{flavor} is yummy')

# you'll iterate over a list by the index of the current item in the list.

# but iterate over sequences or over the index looks clumsy
# Built-in function enumerate wraps any iterator with a lazy generator.
# enumerate yields pairs of the loop index and the next value from the given iterator.
it = enumerate(flavor_list)
print(next(it))
print(next(it))

# unpacking a sequence with the enumerate function, the second parameter is the start index.
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i} : {flavor}')

# things to remember:
# enumerate provides concise syntax for looping over an iterator and getting the index of each
# item from the iterator as you go.

# Prefer enumerate instead of looping over a range and indexing into a sequence

# you can supply a second parameter to enumerate to specify the number from which to begin counting(zero is default)


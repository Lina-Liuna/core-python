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

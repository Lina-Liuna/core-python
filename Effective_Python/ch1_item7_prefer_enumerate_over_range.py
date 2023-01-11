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


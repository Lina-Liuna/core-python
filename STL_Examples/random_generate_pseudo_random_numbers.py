import random

# Random float: 0.0 <= x < 1.0
random_float = random.random()
print(random_float)

# random float: 2.5 <= x <= 10.0
random_float = random.uniform(2.5, 10.0)
print(random_float)

# Integer from 0 to 999 inclusive
random_integer = random.randrange(1000)
print(random_integer)

# Even Integer from 0 to 100 inclusive
random_integer = random.randrange(0, 101, 2)
print(random_integer)

s = 'Those fat cats in government do not care about the poor'
l = s.split(' ')
random_choice = random.choice(l)
print(random_choice)

deck = s.split()
#To shuffle an immutable sequence and return a new shuffled list
random.shuffle(deck)
print(deck)

# Four samples without replacement
random_sample = random.sample([10, 20, 30, 40, 50], k=4)
print(random_sample)
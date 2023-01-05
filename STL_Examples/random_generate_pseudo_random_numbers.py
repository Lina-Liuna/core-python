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
# To shuffle an immutable sequence and return a new shuffled list
random.shuffle(deck)
print(deck)

# Four samples without replacement
random_sample = random.sample([10, 20, 30, 40, 50], k=4)
print(random_sample)

print(help(random.choices))
random_choice = random.choices(['apple', 'orange', 'pineapple'], k=6)
print(random_choice)

# random.choices return a k sized list of popluation elements chosen with replacement
# [20, 0, 5] is the weighs
random_choice = random.choices(['apple', 'orange', 'pineapple'], [20, 0, 5], k=6)
print(random_choice)

# Deal 20 cards without replacement from a deck of 52 playing cards
# determine the proportion of cards with a ten-value: ten, jack, queen, or king.
# here k is the count of populations
# sample(['red', 'blue'], counts=[4, 2], k=5) is equal to sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
print(help(random.sample))
dealt = random.sample(['ten, jack, queen, king','a2-9'], counts=[9, 6], k=15)
print(dealt)
print(dealt.count('a2-9') / 15)


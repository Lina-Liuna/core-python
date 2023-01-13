# Problem:
# Often in python you find yourself with many lists of related objects
# list comprehensions make it easy to take a source list and get a derived list by applying an expression.

phrasal_verbs = ['call off', 'bring up', 'come up', 'hand over', 'talk over', 'go over']
counts = [len(n) for n in phrasal_verbs]

# find longest phrasal verb in verb list:
max_count = 0
longest_name = str()
for name, count in zip(phrasal_verbs, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(max_count, longest_name)

# beware of zip's behavior when the input iterators are of different lengths.
# example:
phrasal_verbs.append('catch up')
for name, count in zip(phrasal_verbs, counts):
    print(name, count)   # No catch up print


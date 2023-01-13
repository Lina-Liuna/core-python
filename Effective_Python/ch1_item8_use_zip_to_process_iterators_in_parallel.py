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
    print(name, count)  # No catch up print

# why new append item not worked?
# because this is how zip works:
# zip keeps yielding tuples until any one of the wrapped iterators is exhausted.
# zip output is as long as its shortest input
# the truncating behavior of zip is surprising and bad.

# if you don't expect the lengths of the lists passed to zip to be equal, consider using
# zip_longest function from the itertools built-in module instead:

import itertools

for name, count in itertools.zip_longest(phrasal_verbs, counts):
    print(f'{name}: {count}')

# things to remember:
# the zip func can be used to iterate over multiple iterators in parallel
# zip create lazy generator that produces tuples, so it can be used on infinitely long inputs.
# zip truncates its output silently to the shortest iterator if you supply it with iterators of different lengths
# use the zip_longest function from itertools

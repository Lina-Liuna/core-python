# Collections module implements specialized container datatypes providing alternative to Python's general purpose
# built-in containers dict, list, set and tuple.

# collections.ChainMap(*maps)
# A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit.
# It is often much faster than creating a new dictionary and running multiple update() calls.
# The class can be used to simulate nested scopes and is useful in templating.

# A ChainMap groups multiple dicts or other mappings together to create a single, updateable view.
# If no maps are specified, a single empty dictionary is provided so that a new chain always has  at least one  mapping.
import collections

questions_meaning = {'who': 'person',
                     'where': 'place',
                     'why': 'reason',
                     'when': 'time',
                     'how': 'manner',
                     'what': 'idea, action',
                     'which': 'choice'}
example_answer = {
    'who is that guy?': 'That is Mike',
    'Where do you live?': 'In Bay Area',
    'why are you leaving?': 'Because I am Tired.',
    'when did you leave?': 'After finish my work',
    'How are you going to Canada?': 'By car',
    'What do you eat for breafast?': 'Chinese pancake made by myself',
    'Which car do you like?': "The White one"
}

mapping_result = list(collections.ChainMap(example_answer, questions_meaning))
print(mapping_result)

combined = questions_meaning.copy()
combined.update(example_answer)
mapping_result = list(combined)

print(mapping_result)

# This section shows various approaches to working with chained maps.
# Examples of simulating Pythons' internal lookup chain:
import builtins

pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
print(list(pylookup))

# Example of letting user specified command-line arguments take precedence over environment variables
# which in turn take precedence over default values:
import os, argparse

defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

print(command_line_args)
combined = collections.ChainMap(command_line_args, os.environ, defaults)
print(combined)
print(list(combined))
print(combined['color'])
print(combined['user'])

combined = collections.ChainMap(os.environ, defaults)
print(combined)
print(list(combined))
print(combined['color'])
print(combined['user'])

# Counter Objects
# A counter tool is provided to support convenient and rapid tallies.
s = 'If you are not willing to learn, no one can help you. If you are determined to learn, no one can stop you.'
cnt = collections.Counter()
l = s.split(' ')
print(l)
for word in l:
    cnt[word] += 1

print(cnt)

# Find the ten most common words in ../README.md
import re
words = re.findall(r'\w+', open('../README.md').read().lower())
print(collections.Counter(words).most_common(10))


# A counter is a dict subclass for counting hashable objects.
# It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

print(dir(collections.Counter))


# deque objects
d = collections.deque('I do not approve of this behavior')
for elem in d:
    print(elem.upper())

d = collections.deque('arm')
d.append('s')
d.appendleft('F')
print(d)
d.pop()
d.popleft()
print(list(d))
d.extend('hand')
print(list(d))
d.extendleft('hand')
print(list(d))

# defaultdict Examples
# Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists.
s = zip('abcba','12345')
l = list(s)
print(l)
d = collections.defaultdict(list)
for k, v in l:
    d[k].append(v)

print(sorted(d.items()))

s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1

print(sorted(d.items()))

# setting the default factory to set makes the defaultdict useful for building a dictionary of sets
s = zip('abcba','12345')
l = list(s)
print(l)
d = collections.defaultdict(set)
for k, v in l:
    d[k].add(v)

print(sorted(d.items()))

# namedtuple() Factory function for tuples with named fields
# Named tuples assign meaning to each position in a tuple and allow for more readable, self documenting code.

# Basic Examples
Point = collections.namedtuple('Point', ['a', 'b'])
p = Point(10, 11)
print(p[0] + p[1])
print(p.a + p.b)
print(p)

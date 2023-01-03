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

# Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3 modules:
import csv
import create_csv_file_writing_content_to_it
import os
header = ['name', 'age', 'title', 'department', 'paygrade']
data = [['Betty', '58', 'CEO', 'IT', '20'],
        ['Morgan', '68', 'CTO', 'IT', '19']
        ]
create_csv_file_writing_content_to_it.create_and_write('employees.csv', header, data)

EmployeeRecord = collections.namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
csv_file_content = csv.reader(open('employees.csv', "rt", encoding='UTF8'))
for emp in map(EmployeeRecord._make, csv_file_content):
    print(emp.name, emp.title)
os.remove('employees.csv')
import sqlite3
import creat_database_using_sqllite3
creat_database_using_sqllite3.create_db_sqllite3()
conn = sqlite3.connect('companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)

os.remove('companydata')
# namedtuyple.fields, tuple of strings listing the field names.
# Useful for introspection and for creating new named tuple types from existing named tuples.
# Basic Examples
Point = collections.namedtuple('Point', ['a', 'b'])
p = Point(10, 11)
Color = collections.namedtuple('Color', 'white yellow green')
Pixel = collections.namedtuple('Pixel', Point._fields + Color._fields)
print(Pixel(11, 22, 255, 255, 255))


# using _fields to simply create a new named tuple typ from the _field attributes
Point3D = collections.namedtuple('Point3D', Point._fields + ('z',))

























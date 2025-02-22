# List Sort method

# The list built-in type provides a sort method for ordering the items in a list instance based on a
# variety of criteria.

# By default, sort will order a list's contents by the natural ascending order of the items.

# The sort method works for nearly all built-in types(strings, floats, etc.) that have a natural ordering to them.

# How to sort a dictionary by keys?
import collections

new_words = collections.defaultdict(list)
new_words = {
    'stride': ['walk with long, decisive steps.', 'he strode across the road'],
    'collation': ['the action of collating something or a light informal meal', 'data management and collation, lunch '
                                                                                'wwas a collation of salami, olives, '
                                                                                'and rye bread'],
    'trivial': ['of little value or importance', 'the story spends too much time on trivial matters'],
    'reliant': ['dependent on someone or something', 'self-reliant'],
    'oars': ['a pole with a flat blade, pivoting in an oar lock, used to row or steer a boat through the water.', ''],
    'conviction': ['a firmly held belief or opinion',
                   'He said he was enjoying his new job, but his voice lacked conviction'],
}
print('Unsorted:', repr(new_words))
# list(new_words.items()).sort(key=lambda x: x.keys)
# res = sorted(new_words_lists, key=lambda x: x[k])
res = collections.OrderedDict(sorted(new_words.items()))
print('\nSorted:  ', res.keys())


# What does Sort do with objects?

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(
            self):  # __repr__() func returns the object representation in string format, can be used to reconstruct the object
        return f'Tool({self.name!r}, {self.weight})'


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]

# use the lambda keywords to define a function for the key parameter that enables me to sort the list of Tool objects
print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted:', tools)

# the lambda function passed as the key parameter can be index to items(sequences, tuples, and dictionaries)
# you may use the key function to do transformations on the values before sorting.
places = ['shanghai', 'New york', 'Beijing', 'dublin']
places.sort()
print('Case sensitive:', places)
places.sort(key=lambda x: x.lower())
print('Case insensitive:', places)

# what if we want use multiple criteria for sorting?
# I have a list of power tools and I want to sort them first by weight, and then by name.

power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

# we can use tuple comparison in order, Solution: define a key function that returns a tuple containing the two
# attributes that I want to sort on in order of priority.

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

# what is the limitation of having the key function return a tuple?
# the limitations: the direction of sorting for all criteria must be the same
# (either all in ascending order, or all in descending order)

power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
print(power_tools)

# What if I want one in ascending and other in descending?

power_tools.sort(key=lambda x: x.name)  # name ascending
power_tools.sort(key=lambda x: x.weight, reverse=True)  # weight descending
print(power_tools)

# things to remember:
# The sort method of the list type can be used to rearrange list's contents by natural ordering

# the key parameter of the sort method can be used to supply a helper function that returns the value to use
# for sorting in place of each item from the list.

# returning a tuple from the key function allows you to combine multiple sorting criteria together.

# you can combine many sorting criteria together by calling the sort method multiple times using different key
# functions.

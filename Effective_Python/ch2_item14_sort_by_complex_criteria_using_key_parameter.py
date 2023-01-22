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
#list(new_words.items()).sort(key=lambda x: x.keys)
#res = sorted(new_words_lists, key=lambda x: x[k])
res = collections.OrderedDict(sorted(new_words.items()))
print('\nSorted:  ', res.keys())


# What does Sort do with objects?

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):        # __repr__() func returns the object representation in string format, can be used to reconstruct the object
        return f'Tool({self.name!r}, {self.weight})'


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]

# use the lambda keywords to define a function for the key parrameter that enables me to sort the list of Tool objects
print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted:', tools)
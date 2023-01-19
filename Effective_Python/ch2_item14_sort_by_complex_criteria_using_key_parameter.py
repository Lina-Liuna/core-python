# List Sort method

# The list built-in type provides a sort method for ordering the items in a list instance based on a
# variety of criteria.

# By default, sort will order a list's contents by the natural ascending order of the items.

# The sort method works for nearly all built-in types(strings, floats, etc.) that have a natural ordering to them.


# What does Sort do with objects?
import collections

class English_Words:
    def __init__(self, name, meaning):
        self.name = name
        self.meaning = meaning

    def __repr__(self):
        return f'English_Words({self.name!r}: {self.meaning})'

words_list = [
    English_Words('stride', 'walk with long, decisive steps.'),
    English_Words('collation', 'the action of collating something or a light informal meal'),
    English_Words('trivial', 'of little value or importance'),
    English_Words('reliant', 'self-reliant'),
]

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

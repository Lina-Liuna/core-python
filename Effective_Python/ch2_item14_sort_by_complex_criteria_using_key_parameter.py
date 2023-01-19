# List Sort method

# The list built-in type provides a sort method for ordering the items in a list instance based on a
# variety of criteria.

# By default, sort will order a list's contents by the natural ascending order of the items.

# The sort method works for nearly all built-in types(strings, floats, etc.) that have a natural ordering to them.


# What does Sort do with objects?

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

print('Unsorted:', repr(words_list))
words_list.sort(key=lambda x: x.name)
print('\nSorted:  ', words_list)

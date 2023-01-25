# NOTE about collections.OrderedDict:
# If you need to handle a high rate of key insertions and popitem calls, OrderedDict may be a better fit
# You shouldn't always assume that insertion ordering behavior will be present when you're handling dictionaries.
# Python makes it easy for programmers to define their own custom container types

votes = {
    'Joe Biden': 306,
    'Trump': 304,
    'Obama':365,
    'Bush': 286,
    'Clinton': 379,
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

ranks = dict()
populate_ranks(votes, ranks)
print(ranks)

def get_winner(ranks):
    return next(iter(ranks))
print(get_winner(ranks))


# rank the votes in alphabetical order instead of rand order
#
# use the collections.abc built-in module to define a new
# dictionary-like class that iterates its contents in alphabetical order.

from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

#
from typing import Dict, MutableMapping


def populate_ranks_2(votes: Dict[str, int],
                   ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner_2(ranks:Dict[str, int]) -> str:
    return next(iter(ranks))

class SortedDict2(MutableMapping[str, int]):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)

sorted_ranks_2 = SortedDict2()
populate_ranks_2(votes, sorted_ranks_2)
print(sorted_ranks_2.data)
winner = get_winner_2(sorted_ranks_2)
print(winner)


# Things to remember:

# Since Python 3.7, you can rely on the fact that iterating a dict instances contents will occur in the same order
# in which the keys were initially added.

# Python makes it easy to define objects that act like dictionaries but that are not dict instances.
# For these types, you can't assume that insertion ordering will be preserved.

# There are three ways to be careful about dictionary-like classes:
# Write code that doesn't rely on insertion ordering.
# Explicitly check for the dict type at runtime
# require dict types using type annotations and static analysis.



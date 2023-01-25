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


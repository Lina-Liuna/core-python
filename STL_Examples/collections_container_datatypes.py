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
    'How are you going to Canada?':'By car',
    'What do you eat for breafast?': 'Chinese pancake made by myself',
    'Which color of the car do you like?': "The White one"
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

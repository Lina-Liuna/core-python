# The three fundamental operations for interacting with dictionaries:
# 1. accessing
# 2. assigning
# 3. deleting keys and their associated values

# The contents of dictionaries are dynamic, and thus it's entirely possible - even likely -- when you try to access or
# delete a key, it won't already be present.
import collections

# Counter class in collections, counter will hod the count of each of the elements present in the container,

# The counter holds the data in an unordered collection, just like hashable objects,
# the elements here represent the keys and the count as values
# counter class allows you to count the items in  an iterable list.
# arithmetic operations like addition, subtraction, intersection, and union can be easily performed on a counter

counter_class = collections.Counter()

restaurant_counters = {
    'kio palace': 5,
    'Imperial Delight': 4,
    'Peking Delight' : 3,
    'Szechuan Restaurant': 2,
}
key = 'lulu'
count = restaurant_counters.get(key, 0)
restaurant_counters[key] = count + 1
print(restaurant_counters.items())

restaurant_votes = {
    'koi palace': ['Nathan', 'Alice'],
    'Imperial Delight': ['Ali', 'Joe'],
}

key = 'peking delight'
who = 'Kevin'

if (names := restaurant_votes.get(key)) is None:
    restaurant_votes[key] = names = []
    names.append(who)

# the dict provides the setdefault method to help shorten this pattern
# setdefault tries to fetch the value of a key in the dictionary,
# if the key isn't present, the method assigns that key to default value provided.
# the setdefault returns the value of that key.

names = restaurant_votes.setdefault(key, [])
names.append(who)

# side-effect of setdefault:
# the default value passed to setdefault is assigned directly into the dictionary when the key is missing instead of
# being copied.
data = {}
key = 'tricky'
value = []
data.setdefault(key, value)
print('before:', data)
value.append('tricky setdefault')
print('after:', data)

# Things to remember:
# There are four common ways to detect and handle missing keys in dictionary: using in , keyError,
# get method, setdefault method

# the get method is best for dict that contain basic types like counters, and it is preferable along with assignment
# expressions when creating dictionary values has a high cost or may raise exceptions

# when the setdefault method of dict seems like the best fit for your problem,
# you should consider using defaultdict instead


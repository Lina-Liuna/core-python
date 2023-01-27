# The three fundamental operations for interacting with dictionaries:
# 1. accessing
# 2. assigning
# 3. deleting keys and their associated values

# The contents of dictionaries are dynamic, and thus it's entirely possible - even likely -- when you try to access or
# delete a key, it won't already be present.


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


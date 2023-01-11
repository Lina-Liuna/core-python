# tuple used to create immutable, ordered sequence of values.
# A tuple is a pair of two values, such as keys and values from a dictionary

lina_food_calories = {
    'kirkland oat milk': 100,
    'vegetables': 30,
    'berries': 50,
    'nuts': 150,
}
# dict.items() return a view objects, return a new view of the dictionary's items(key, value) pairs
# what's the view object?
# The view object provide a dynamic view on the dictionary's entries, which means that when the dictionary
# changes, the view reflects these changes.
print(lina_food_calories.items())

items = set(lina_food_calories.items())
print(items)

items = list(lina_food_calories.items())
print(items)

items = tuple(lina_food_calories.items())
print(items)

# values in tuple can be accessed through numerical indexes
item = ('cucumber', 'red round pepper')
first = item[0]
second = item[1]
print(first, 'and', second)

first, second = item # unpacking
print(first, 'and', second)

item = (('cucumber', 30), ('red round pepper', 20))
first, second = item # unpacking
print(first, 'and', second)

# once a tuple is created, you can not modify it by assigning a new value to an index.
# tuple object does not support item assignment

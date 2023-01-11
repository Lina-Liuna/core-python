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


# unpacking works when assigning to lists, sequences, and multiple levels of arbitrary iterables with iterables

lina_favorite_snacks = {
    'salty': ('pistachio', 150),
    'sweet': ('data', 180),
    'veggie':('red pepper', 30),
    'fruit':('berries', 30),
}

(
    (type1, (name1, cals1)),
    (type2, (name2, cals2)),
    (type3, (name3, cals3)),
    (type4, (name4, cals4))
) = lina_favorite_snacks.items()

print(f'Lina Favorite {type1} is {name1} with {cals1} calories')
print(f'Lina Favorite {type2} is {name2} with {cals2} calories')
print(f'Lina Favorite {type3} is {name3} with {cals3} calories')
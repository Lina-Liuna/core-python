# what to do if we want the first two items of the item with unpacking?
car_ages = [0, 7, 9, 4,3, 10, 6, 12, 23, 18]
car_ages_descending = sorted(car_ages, reverse=True)

# we want find the oldest and the second oldest car
#oldest, second_oldest = car_ages_descending        # error: too many values to unpack

# unpacking through a starred expression
oldest, second_oldest,  *others = car_ages_descending
print(oldest, second_oldest, *others)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest)


# to unpacking assignment that contain a starred expression, you must have at least one required part, or error.
# *others = car_age_descending # Error

# you can't use multiple catch-all expressions in a single-level unpacking pattern:
# first, *middle, *second_middle, last = xxxx # Error

kids_play = {
    'Amusement Park' : ('Great America', 'Gilroy Garden', 'Six Flags'),
    'Museum' : ('Blackhawk Museum', 'MOMA', 'Kids Discovery')
}

((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = kids_play.items()
print(f'Best at {loc1} is {best1}, {len(rest1)} others')
print(f'Best at {loc2} is {best2}, {len(rest2)} others')
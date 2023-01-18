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
print(f'Best of {loc1} is {best1}, {len(rest1)} others')
print(f'Best of {loc2} is {best2}, {len(rest2)} others')


def generate_car_info():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    yield ('1992', 'Range Rover', 'Evoque', '2022', '$51-000')

it = generate_car_info()
header, *rows = it
print('Car Info Header:',header)
print('Row Count:', len(rows))


# Things to Remember:
# Unpacking assignment may use a starred expression to catch all values that weren't assigned to
# the other parts of the unpacking pattern into a list.
#
# Starred expression may appear in any position, and they will
# always become a list containing the zero or more values they receive.

# when dividing a list into non-overlapping pieces, catch-all unpacking is much less error prone than slicing and
# indexing


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
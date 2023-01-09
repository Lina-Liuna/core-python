# why c-format string not good enough, example:
print('Use tuple formatting:')
pantry = [('cherries', 1),
          ('blueberry', 3),
          ('raspberry', 1)]

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))

print("Use Tuple formatting, making a few code modifications")
# imporve:
# Make a few modifications to the values that I'm formatting to make the printed message more useful.
# !!!!!Problem 1!!!!!!!!!
# causes the tuple in the formatting expression to become so long that it needs to be split across lines
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' %(
        i + 1,
        item.title(),
        round(count)
    ))

# Solution of problem 1, but:
# dictionary format strings introduce and exacerbate other issues
# formatting expressions become longer and
# more visually noisy because of the presence of the dictionary key and
# colon operator on the right side.
# To help solve some of these problems, the % operator in Python has
# the ability to also do formatting with a dictionary instead of a tuple. The
# keys from the dictionary are matched with format specifiers with the
# corresponding name, such as %(key)s
print("use dictionary formatting:")
for i, (item, count) in enumerate(pantry):
    print('#%(loop)d: %(item)-10s = %(count)d' % {
        'loop': i+1,
        'item': item.title(),
        'count': round(count)
    }
          )
print("Using F formatting:")
for i, (item, count) in enumerate(pantry):
    f_string = f'#{i + 1}: {item.title():<10} = {round(count):>10}'
    print(f_string)

#!!!!!!problem 2!!!!!
# use the same value in a format string multiple times, you have to repeat it in the right side tuple:
template = '%s loves health food, please see %s cook.'
name = 'Lina Liu'
formatted = template %(name, name)
print(formatted)

# Solution of problem 2, but:
# Using dictionaries in formatting expressions also increases verbosity
template = '%(name)s loves health food, please see %(name)s cook.'
name = 'Lina Liu'
formatted = template % {'name': name}
print(formatted)

# Soultion of problem 2:
formatted = '{0} loves healthy food, please see {0} cook.'.format(name)
print(formatted)

f_string = f'{name} loves healthy food, please see {name} cook'
print(f_string)

menu = {
    'soup 1': 'Californian Clam Chowder',
    'soup 2': 'Chilled Avocado Soup',
    'soup 3': 'Cream of Mushroom Soup',
    'Oyster 1': 'West Coast Oysters',
    'Oyster 2': 'Kumamoto',
    'Specials': 'Schnitzel',
}

template = ('Today\'s soup is %(soup 1)s,'
            'Oyster is %(Oyster 2)s,'
            'Special entree is %(Specials)s'
            )
formatted = template % menu
print(formatted)

# Within the braces you may also specify the positional index of an argument passed to the format method to use for
# replacing the placeholder. This allows the format string to be updated to reorder the output without requiring you
# to also change the right side of the formatting expression

key = 'water'
value = '500ml'

formatted = '{1} = {0}'.format(key, value)
print(formatted)

formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key:<10} = {value: >10}'
print(formatted)











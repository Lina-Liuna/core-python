# why c-format string not good enough, example:
pantry = [('cherries', 1),
          ('blueberry', 3),
          ('raspberry', 1)]

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))

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

for i, (item, count) in enumerate(pantry):
    print('#%(loop)d: %(item)-10s = %(count)d' % {
        'loop': i+1,
        'item': item.title(),
        'count': round(count)
    }
          )


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














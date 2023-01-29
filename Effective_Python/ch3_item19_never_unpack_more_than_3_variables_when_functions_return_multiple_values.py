# if you return more than 3 values, especially return values are numeric:
#
# it is all to easy to recorder them accidentally.
# which can cause bugs that are hard to spot later.
# Using a large number of return values is extremely error prone.

#For example:
# Correct:
#minimum, maximum, average, median, count = get_stats(lengths)
# Oops! Median and average swapped:
# minimum, maximum, median, average, count = get_stats(lengths)

# Second, the line that calls the functions and unpacks the values is long.

# To avoid these problems, you should never use more than three variables when unpacking the multiple return values.
# the return values can be three-tuple, two variables and one catch-all starred expression or namedtuple.

def get_avg_ratio(numbers):
    avarage = sum(numbers) / len(numbers)
    scaled = [x / avarage for x in numbers]
    scaled.sort(reverse=True)
    return scaled

number_list = [19, 40, 25, 56, 79, 92, 23]
longest, *middle, shortest = get_avg_ratio(number_list)
print(f'longest: {longest:>4.0%}')
print(f'shortest:{shortest:>4.0%}')

# Things to remember:
# You can have functions return multiple values by putting them in a tuple and having the caller take advantage of
# Pythons' unpacking syntax.

# Multiple return values from a function can also be unpacked by catch-all starred expressions.

# Unpacking into four or more variables is error prone and should be avoided, instead return a small class or namedtuple instance.


# namedtuple examples
# namedtuple() Factory function for tuples with named fields
# Named tuples assign meaning to each position in a tuple and allow for more readable, self documenting code.
import collections
# Basic Examples
Point = collections.namedtuple('Point', ['a', 'b'])
p = Point(10, 11)
print(p[0] + p[1])
print(p.a + p.b)
print(p)


# namedtuple.fields, tuple of strings listing the field names.
# Useful for introspection and for creating new named tuple types from existing named tuples.
# Basic Examples
Point = collections.namedtuple('Point', ['a', 'b'])
p = Point(10, 11)
Color = collections.namedtuple('Color', 'white yellow green')
Pixel = collections.namedtuple('Pixel', Point._fields + Color._fields)
print(Pixel(11, 22, 255, 255, 255))


# using _fields to simply create a new named tuple typ from the _field attributes
Point3D = collections.namedtuple('Point3D', Point._fields + ('z',))

# __doc__ can be customized by making direct assignments to the __doc__ fields
Book = collections.namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title'
Book.authors.__doc__ = 'Authors'

print(Book("1234567890123", 'The subtle Art of Noting Giving A F', 'Mark Manson'))



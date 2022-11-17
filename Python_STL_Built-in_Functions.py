# bin() convert an integer number to a binary string prefixed with 0b
print(bin(11))
print(bin(-11))
print(hex(255))
print(hex(-250))

print(format(11, '#b'))
print(format(11, 'b'))
print(format(11, '#x'))
print(format(11, 'x'))

# dir()
import struct
print(dir())
print(dir(struct))

class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']

s = Shape()
print(dir(s))


seasons = ['spring', 'summer', 'fall', 'winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))


def enumerate_new(sequences, start=0):
    n = start
    for elem in sequences:
        yield n, elem
        n += 1

print(list(enumerate_new(seasons)))


x = 5
y = 10
print(eval('x*x + y*y'))
print(eval('sum([2,4,6,8,10])'))

print(float('2.1415926'))


s = input('please enter your name:')
print(s)



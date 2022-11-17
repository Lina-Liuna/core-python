# bin() convert an integer number to a binary string prefixed with 0b
print(bin(11))
print(bin(-11))
print(hex(255))
print(hex(-250))
print(oct(255))
print(oct(-250))

print(format(11, '#b'))
print(format(11, 'b'))
print(format(11, '#x'))
print(format(11, 'x'))
print(format(11, '#o'))
print(format(11, 'o'))

# pow example
print(pow(2,4))
print(pow(3,3))


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

#iter() example
fruit = ['blueberry', 'raspberry', 'apple']
fruit_iter = iter(fruit)
print(next(fruit_iter))
print(next(fruit_iter))
print(next(fruit_iter))

# implement iter() for custom object
class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max:     #funny things happens if you remove "="
            raise StopIteration
        self.num += 1
        return self.num

pn = PrintNumber(4)
pn_iter = iter(pn)
print(next(pn_iter))
print(next(pn_iter))
print(next(pn_iter))
print(next(pn_iter))
#print(next(pn_iter))


# So funny, NotImplementedError: dir_fd unavailable on this platform!!!!!!!
#import os
#dir_fd = os.open('/Users/lina/code/core-python/', os.O_RDONLY)
#def operner(path, flags):
    #print('not implemented!')
    #return os.open(path, flags, dir_fd=dir_fd)

#with open('test_file.txt', 'a', opener=operner) as f:
#with open('test_file.txt', 'a') as f:
    #print('This will be written to xxxx/test_file.txt', file=f)

#os.close(dir_fd)

# zip(*iterables, strict=False)
# iterate over several iterables in parallel, producing tuples with an item from each one
for item in zip([1, 2, 3,], ['berry', 'apple', 'cucumber'], ['favorite No. 1', 'favorite No. 2', 'favorite No. 3']):
    print(item)

print(list(zip([1, 2, 3,], ['berry', 'apple', 'cucumber'], ['favorite No. 1', 'favorite No. 2', 'favorite No. 3'])))
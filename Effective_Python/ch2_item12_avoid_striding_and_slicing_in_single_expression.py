
# Python has special syntax for the stride of a slice in the form somelist[start:end:stride]
# somelist[start:end:stride] let you take every nth item when slicing a sequence.
# if only stride, it will like: somelist[::stride]
# stride makes it easy to group by even and odd indexes in a list:
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = rainbow[::2]
evens = rainbow[1::2]
print(odds)
print(evens)

# problem in stride: causes unexpected behavior that can introduce bugs.
# common python trick for reversing a byte string:
# slice the string with a stride of -1:
x = '中文'
y = x[::-1]
print(y)

x = b'mongoose'
y = x[::-1]
print(y)

# bugs: strides not work on UTF-8 byte string:
w = '中文'
x = w.encode('utf-8')
y = x[::-1]
# z = y.decode('utf-8') UnicodeDecodeError: 'utf-8' codec can't decode byte 0x87 in position 0: invalid start byte

x = [1, 2, 3, 4, 5, 6, 7, 8]

# Negative stride besides -1 useful:
print(x[::2])
print(x[::-2])
print(x[2::2])
print(x[-2::-2])
print(x[-2:2-2])
print(x[2:2-2])

# the point is the stride part of the slicing syntax can be extremely confusing.
# having three numbers within the brackets is hard enough to read because of its density.
# suggestions: avoid using a stride along with start and end indexes.
# if you must use a stride, prefer making it a positive value and omit start and end indexes.
y = x[::2]
z = y[1:-1]
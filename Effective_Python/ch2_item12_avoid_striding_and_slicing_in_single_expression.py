
# Python has special syntax for the stride of a slice in the form somelist[start:end:stride]
# somelist[start:end:stride] let you take every nth item when slicing a sequence.
# if only stride, it will like: somelist[::stride]
# stride makes it easy to group by even and odd indexes in a list:
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = rainbow[::2]
evens = rainbow[1::2]
print(odds)
print(evens)
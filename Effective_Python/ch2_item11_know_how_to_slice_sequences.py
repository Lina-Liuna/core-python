# basic form of the slicing syntax is somlist[start:end], start is inclusive, end is exclusive
s = 'a b c d e f g h'
a = s.split(' ')
print(a)
print(a[:])
print(a[:5])
print(a[:-1])
print(a[-3:])
print(a[2:-1])

# using negative numbers for slicing is helpful for doing offsets relative to the end of a list.

# slicing index beyond the boundaries of a list by silently omitting missing items.
print(a[:20])
print(a[-20:])
# The result of slicing a list is a whole new list.
# Modifying the result of slicing won't affect the original list
b = a[3:]
print(b)
b[1] = 99
print(b)
print(a)

# the slice replace length: the length of slice assignment don't need to be the same.
# shrinks the list
print(a)
a[2:] = [100, 99, 3]
print(a)

# grows a list
s = 'a b c d e f g h'
a = s.split(' ')
a[2:3] = [11,22,33,44,55]
print(a)

s = 'a b c d e f g h'
a = s.split(' ')

# copy of the original list
b = a[:]
b[1:] = [2]
print(a)

# reference a list
b = a
b[1:] = [2]
print(a)


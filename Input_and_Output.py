#formatted string literals
year = 2022
event = 'Rferendum'
fmt_str = f'Results of the {year} {event}'
print(fmt_str)

#str.format
yes_vote = 42_572_654
no_vote = 43_132_495

percentage = yes_vote / (yes_vote + no_vote)
print('{:-9} YES votes {:2.2%}'.format(yes_vote, percentage))
print('{:-8} YES votes {:2.2%}'.format(yes_vote, percentage))
print('{} YES votes {:2.2%}'.format(yes_vote, percentage))

#using repr() function or str() function to convert any value to a string
s = 'Hello, Friend.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

#The repr() of a string adds string quotes and backslashes:
hello = 'hello, worlds\n'
hellos = repr(hello)
helloss = str(hello)
print(hellos)
print(helloss)

#the argument to repr() may be any python object:
print(repr((x,y,('spam', 'eggs'))))

import math
print(f'The value of Pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

#Modifiers '!r'
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

#= specifier used to expand an expression to the text of the expression
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

#string format() method
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

#A number in the brackets can be used to refer to the postion of the object passed into the str.format() method
print('{0} and {1}'.format('spam', 'egg'))
print('{1} and {0}'.format('spam', 'egg'))

#if keyword arguments are used in the str.format() method, their values are referred to by using the name ofthe argument.
print('This {food} is {adjective}.'.format(food='spam', adjective='absoluttely horrible'))

#positional and keyword arguments can be arbitrarily combined:
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

#what to do if you have a long string and you don't want to split it up?
#passing the dict and using square brackets [] to access the keys
table = {'Sjoered': 4127, 'Jack': 4098, 'Dcab':8647}
print('Jack:{0[Jack]:d}; Sjoered:{0[Sjoered]:d};Dcab:{0[Dcab]:d}'.format(table))
print('Jack:{Jack:d}; Sjoered:{Sjoered:d};Dcab:{Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


#str.rjust()/str.ljust()/str.center()
for x in range(1, 11):
    print(str(x).rjust(2), str(x*x).rjust(3), str(x*x*x).rjust(4))


#str.zfill()
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

#old string formatting
import math
print('The value of pi is approximately %5.3f.' %math.pi)
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
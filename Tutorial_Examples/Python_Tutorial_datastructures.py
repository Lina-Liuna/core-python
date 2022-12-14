

#Python Tutorial Data Structure list methods silly examples
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.extend(['grape', 'mango','cucumber'])
print(fruits)
fruits.insert(0, 'strawberry')
fruits.insert(len(fruits), 'watermelon')
print(fruits)
fruits.remove('apple')
print(fruits)
print(fruits.pop())
print(fruits.pop(5))
print(fruits.index('pear'))
print(fruits.count("apple"))
#print(fruits.sort())
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
bakup_fruits = fruits.copy()
print(bakup_fruits)

#using lists as stacks
stack = [3, 4, 5]
stack.append(8)
print(stack.pop())
print(stack)

#using collections.deque as queues
from collections import deque
queue = deque(['Eric', 'John', 'Michael Rosen'])
queue.append('Terry')
queue.append('Graham')
print(queue.popleft())
print(queue.popleft())
print(queue)

#List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)  #each element is the result of some operations applied to each memeber of another sequence.

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)] #list comprehension consists of brackets containing an expression followed by a for clause
print(squares)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y ])

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x > 0])
print([abs(x) for x in vec]),

freshfruit = ['banana', 'loganberry', 'passion fruit']
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(10)])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

#list comprehensions can contain complex expressions and nested functions:
from math import pi
print([str(round(pi, i)) for i in range(6)])

#the list comprehensions will transpose rows and columns:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

#in the real world, you should prefer built-in funcitons to complex flow statements.
#The zip() function would do a great job for this use case:
#call the *operator to unpack the arguments out of a list or tuple
print(list(zip(*matrix)))

#The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

del a

#Tuples
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 3, 5, 7)
print(u)
# t[0] = 10000 # Tuples are immutable, tuple object does not support item assginment.
print(t)

#Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  #show that duplicates have been removed
print('orange' in basket)   #fast membership testing
print('crabgrass' in basket)

#Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)      #unique letters in a
print(b)      #unique letters in a
print(a-b)    #letters in a but not in b
print(a | b)  #letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both


a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

#small examples using a dictionary
tel = {'jacky': 4098, 'scape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jacky'])
del tel['scape']
tel['irv'] = 4129
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jacky' not in tel)

print(dict([('scape', 4139), ('guido', 4127), ('jacky', 4098)]))

print({x:x**2 for x in range(6)})

#when the keys are simple strings, it is sometimes earier to specify pairs using keyword arguments
print(dict(scape=4139, guido=4127, jacky=4098))


#using items() method to looping through dictionaries, the key and corresponding value can be retrieved at the same time
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

#sequence using enumerate() function to retrieve the position index and corresponding value at the same time
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#using zip() function to loop over two or more sequences at the same time
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0}? It is {1}'.format(q, a))

#using sorted() function to loop over a sequence in sorted order, sorted() function return a new sorted list while leaving the source unaltered
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
print('-------set() example-------')
#using set() function on a sequence to eliminate duplicate elements
for f in set(basket):
    print(f)

print('----------set() and sorted() func------------')
#using set() combine with sorted() function over a sequence is an idiomatic way to loop over unique elements in sorted order
for f in sorted(set(basket)):
    print(f)


#a list may changed while you are looping over it, so, it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
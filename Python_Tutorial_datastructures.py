

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



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

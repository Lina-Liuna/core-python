n = 32
print(bin(n))
print(n.bit_length())

# print(n.bit_count())
print(dir(n))

print((1024).to_bytes(4, byteorder='big'))
print((65).to_bytes(2, byteorder='big'))

def bit_length(self):
    s = bin(self)
    s = s.lstrip('-0b')
    return len(s)

# 'in' and 'not in' operations used as subsequence testing
print('app' in 'apple')

# items in the sequence s are not copied; they are referenced multiple times
# Wow, amazing reference instead of copy examples for the sequence.
lists = [] * 3
print(lists)

listss = [[]] * 3
print(listss)
print(listss[0])
listss[0].append(3)
print(listss)

#Common Sequence operations
l1 = ['apple', 'orange', 'banbana']
l2 = ['berry', 'cherry', 'merry']

l3 = l1 + l2
print(l3)



l3 = l1[0:1:2]
print(l3)

l3 = l1 * 3
print(l3)

print(min(l1), max(l1))
print(l3.count('apple'))

# mutable sequence types operations
s = []
# s[0] = 'peach' list assignment index out of range
s.append('love')
s[0] = 'peach'
s[1:4] = l2
s.append('hary')
print(s)

s2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s2[0:10:2] = s
print(s2)

s3 = s2.copy()
print(s3)

del s3[0:10:2]
print(s2, s3)

s3.clear()
print(s3)
s3 = ['morning lina']
s3 *= 3
print(s3)

s3[0] = 'good morning, Lina'
s3.insert(0, 'Hello')
print(s3)

# QUESTIONS: why [[]] * n and [] * n follows the different rule? tricky and funny.
listss = [[]] * 3
listss[0].append(3)
listss[1].append(5)
print(listss)

s4 = [] * 3
s4.append('test')
print(s4)

s4 *= 10
print(s4)
n1 = [1, 2, 3, 4, 5]
s4[0:10:2] = n1
print(s4)
s4.pop()
print(s4)
s4.pop(0)
print(s4)
s4.remove('test')  #remove the first item from s.
print(s4)
s4.reverse()
print(s4)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  #show that duplicates have been removed

b = basket.copy()
print(b)
b.clear()
print(b)

l = ['a'], ['a', 'b', 'c']
print(l)

l = [i for i in range(0, 20)]
print(l)

l = list(range(1, 10, 2))
print(l)

l = sorted('aecba')
print(l)

l.sort(reverse=True)
print(l)

l = list(range(10))
print(l)

l = list(range(0,-11,3))
print(l)

l = list(range(0,-11,-3))
print(l)


s = '''this triple quote test
        span multi lines'''
print(s)

# only whitespace between them will be implicitly converted to a single string literal
s = "boiled" " eggs"
print(s)

s = str('abc')
print(s)

s = str('this morning I will eat\t toast and yogurt!')
print(s.capitalize())
print(s.casefold())
print(s.center(len(s) + 10, '*')) # original strsing is returned if width is less than or equal to len(s)


print(s.count('i'))
print(s.count('and'))

print(s.endswith("!"))

print(s.expandtabs(tabsize=16)) # default tabsize is 8, giving tab positions at colums 0, 8, 16

print('01\t012\t0123\t01234'.expandtabs())
print('01\t012\t0123\t01234'.expandtabs(4))
print('01\t012\t0123\t01234'.expandtabs(16))


print(s.find('!'))
print('the sum of 1 + 2 is {0}'.format(1+2))

print(s.index('I'))

print(s.isdigit())
print(s.islower())
print('     test lstrip funciton'.lstrip())
print('www.linaliu.com'.lstrip('xyz'))
print('www.linaliu.com'.lstrip('xyz.'))
print('www.linaliu.com'.lstrip('xyw.'))
print(' test rstrip  '.rstrip())
print('linaliu'.rstrip('liu'))

print('MyNameisNa na na na na'.removeprefix('My'))
print('MyNameisNa na na na'.removesuffix('na na na'))



print('1,2,3'.split(','))
print('1,2,3,4'.split(',',maxsplit=2))
print('1 2 3'.split())

print('ab c\n de fg \r kl\r\n'.splitlines())
print('ab c\n de fg \r kl\r\n'.splitlines(keepends=True))

print('#........Book title #32........'.strip('.#!  '))

print('this is book is dangerous'.title())

print('33'.zfill(5))
print('-33'.zfill(5))

s = {c for c in 'magic words abra-ca-da-bra' if c not in 'abc'}
print(s)

s = {'rainny', 'dayff'}
print(s)

s = set(['a', 'b', 'c'])
print(s)

# s = set('a', 'b', 'c')  # TypeError: set expected at most 1 argument, got 3
s = set('abcdefghijklmn')
print(s)

print(len(s))
print('x' in s)
print(s.isdisjoint('lmn'))
print(s.isdisjoint('xyz'))
print(s.issubset('abc'))

s1 = set('lina')
s2 = set('linaliu')
print(s1 <= s2)
print(s2 - s1)

s1 = set('morning')
print(s1 | s2)

print(s1.copy())
s1.add('!!!')
print(s1)
s1.remove('!!!')
print(s1)
s1.clear()
print(s1)

d = dict([('car', 6), ('bar', 3), ('tar', 4)])
print(d)

d = {x: x ** 2 for x in range(10)}
print(d)

d = {'my': 2, 'name': 4, 'is': 6, 'sker':8}
print(d)

s = str('abc')
k = list()
k.append(1)
k *= 3

d = dict(zip(s, k))
print(d)




















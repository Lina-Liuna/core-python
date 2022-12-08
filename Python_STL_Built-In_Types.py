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







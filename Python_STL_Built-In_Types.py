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
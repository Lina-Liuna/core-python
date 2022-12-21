# re - regular expression operations
import re

m = re.search('(?<=abc)def', 'abcdef')
print(m.group())

m = re.search('(?<=c)def', 'abcdef')
print(m.group())

m = re.search('(?<=bc)def', 'abcdef')
print(m.group())

m = re.search('(?<=)def', 'abcdef')
print(m.group())

m = re.search(r'(?<=-)\w+', 'spam-egg')
print(m.group())


m = re.split(r'\w+', 'good morning, beautiful people!')
print(m)
m = re.split(r'\W+', 'good morning, beautiful people!')
print(m)
m = re.split(r'(\W+)', 'good morning, beautiful people!')
print(m)
m = re.split(r'\W+', 'good morning, beautiful people!', 1)
print(m)
m =re.split(r'\W*', 'good morning, beautiful people!')
print(m)

m =re.split(r'\b', 'good morning, beautiful people!')
print(m)
m =re.split(r'\B', 'good morning, beautiful people!')
print(m)
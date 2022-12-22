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

# re.compile(pattern, flags=0)
# this method is used to compile a regular expression pattern into a regular expression object,
# the result of compile method used for matching using its match() and search() methods, which we have discussed above.
# This can save time since parsing/handling regex strings can be computationally expensive to run.

pattern = re.compile('fix')
result = pattern.findall('Put it in backlog. so we can fix it later, right?')
print(result)

pattern = re.compile('fix')
result = pattern.findall('Put it in backlog. so we can fix-it-later, right?')
print(result)

result = pattern.findall('fix it later')
print(result)

pattern = re.compile('L')
result = pattern.search('LinaLiu')
print(result.group())

result = pattern.search('LinaLiu', 1)
print(result.group())

# Error
#result = pattern.search('Lina', 1)
#print(result.group())
























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



pattern = re.compile('L')
result = pattern.search('LinaLiu')
print(result.group())

result = pattern.search('LinaLiu', 1)
print(result.group())

# Error
#result = pattern.search('Lina', 1)
#print(result.group())

# re.findall() return all non-overlapping matches of pattern in string,as a list of strings or tuples
# the string is scanned left-to-right, and matches are returned in the order found.
pattern = re.compile('fix')
result = pattern.findall('Put it in backlog. so we can fix-it-later, right?')
print(result)

result = pattern.findall('fix it later')
print(result)

result = re.findall(r'\bf[a-z]*', 'ready for, grateful for, suitable for, thankful for, prepared for, respected for, responsible for')
print(result)

words = """
'very long=extensive, 
very loose=slack,
 very accurate=Exact, 
 very afraid=Fearful
 very dull=Tedious
 very eager=Keen
 very evil=Wicked
 very fast=Quick
 very fierce=Ferocious
 very lovely=Adorable
"""
result = re.findall(r'(\w+ \w+)=(\w+)', words)
print(result)

coordinate = 'set width=100 height=180 length=250'
result = re.findall(r'(\w+)=(\w+)', coordinate)
print(result)

# re.sub(pattern, replacement, string, count=0, flags=0) sub means substitute
# return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by
# the replacement repl.
# replacement can be a string or a function, if a string, any backslash escapes in it are processed.
# \n is converted to a single newline character, \r is converted to a carriage return
# \6 are replaced with the substring matched by gorup of 6 in the pattern.

result = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
                r'static PyObject*\npy_\1(void)\n{',
                'def myfunc():')
print(result)

result = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
                r'static PyObject*\npy_\0(void)\n{',
                'def myfunc():')
print(result)

# if replacement is a function, it is called for every non-overlapping occurrence of pattern.
# The function takes a single match object argument, and returns the replacement string.

def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'

result = re.sub('-{1,2}',dashrepl, 'pro----gram-files')
print(result)


# what is pattern groups mean?
pattern = re.compile('-')
result = re.search(pattern, 'pro----gram-files')
print(result.group(0))
# print(result.group(1))
print(result.groupdict())

# What is Group in Regex?
# A group is part of regex pattern enclosed in parentheses() metacharacter.
# example
# (cat) create a single group containing the letter c a t.
# ((\w)(\s\d)), there are three such groups:
# ((\w)(\s\d))
# (\w)
# (\s\d)

# where is feel and understand?
string = 'I FEEL you means I UNDERSTAND you'
result = re.search(r'(([A-Z]+)+)', string)
print(result.groups())
print(result.group(0))
print(result.group(1))

result = re.findall(r'([A-Z]+)', string)
print(result)


















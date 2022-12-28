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

# scan through string looking for the first location where this regular expression produces a match.
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
# re.search() Scan through string looking for the first location where the regular expression pattern
# produces a match, and return a corresponding match object.
result = re.search(r'(([A-Z]+)+)', string)
print(result.groups())
print(result.group(0))
print(result.group(1))

result = re.findall(r'([A-Z]+)', string)
print(result)

# re.escape(pattern)
# Escap special characters in Pattern.
# This is useful if you want to match an arbitrary literal string
# that may have regular expression metacharacters in it.
result = re.escape('liuna.lina@gmail.com')
print(result)


#match object examples
match = re.match(r"\w+ \w+", 'I wish you were here')
print(match.group())

match = re.match(r"(\w+) (\w+)", 'I wish you were here')
print(match.group())

print(match.group(1), match.group(2))

# Useful is the followings:
match = re.match(r"(\d+)\.(\d+)", "3.1415926")
print(match.groups())

match = re.match(r"(\w+)\.(\w+)(@)(\w+)", "liuna.lina@gmail.com")
print(match.groups())

# match.start[] and match.end[]
# Return the indices of the start and end of the substring matched by group

email = 'liuna.linaremove_this@gmail.com'
match = re.search('remove_this', email)
print(email[:match.start()] + email[match.end():])

# Regular Expression Examples
# Checking for a Pair

def displaymatch(match):
    if match is None:
        print('Invalid, no match')
        return None
    print('Match: %r, gorups\%r>' %(match.group(), match.groups()))
    return 'Match: %r, gorups\%r>' %(match.group(), match.groups())

# a poker program where a player's hand is represented as a 5-character string with
# each character representing a card,
# 'a' for ace
# 'k' for king
# 'q' for queen
# 'j' for jack
# 't' for 10
# '2-9' representing the card with that value

# to see if a given string is a valid hand, one could do the following:
valid = re.compile(r"^[a2-9tjqk]{5}$")
displaymatch(valid.match('a2345'))
displaymatch(valid.match('tjqka'))
displaymatch(valid.match('akttt'))
displaymatch(valid.match('aaa'))

# Check if contained a pair, or two of the same valued cards.
# dot in the default mode, this matches any character except a newline
# * matches 0 or more repetitions of the preceding RE, ab* will match a, ab,
pair = re.compile(r".*(.).*\1")
displaymatch(pair.match('77755'))
displaymatch(pair.match('12345'))
displaymatch(pair.match('aakkjj'))

# To find out what card the pair consists of, one could use the group() method of the match object
print(pair.match('77755').groups())

print(pair.match('77755').group(1))


# search() va. match()
# Python offers different primitive operations based on regular expressions:
# re.match() checks for a match only at the beginning of the string
# re.search() checks for a match anywhere in the string
# re.fullmatch() checks for entire string to be a match
result = re.match('c', 'abcdef')
print(result)

result = re.search('c', 'abcdef')
print(result)

result = re.match('K.*p', 'I will Keep it under my hat')
print(result)
result = re.search('K.*p', 'I will Keep it under my hat')
print(result)
result = re.fullmatch('K.*p', 'I will Keep it under my hat')
print(result)

result = re.fullmatch('I(.*)K.*p(.*)', 'I will Keep it under my hat')
print(result)










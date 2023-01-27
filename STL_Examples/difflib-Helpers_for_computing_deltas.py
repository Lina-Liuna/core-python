# difflib.context_diff(a,b,formfile=‘’,tofile=‘’,fromfiledate=‘’,tofiledate=‘’,n=3, lineterm=‘\n’
# compare a and b(strings) return a delta(a generator generating the delta lines) in context diff format
# returns a delta(a generator generating the delta lines)
import difflib
import sys

s1 = ['cat\n', 'best\n', 'man\n', 'Good Morning!\n']
s2 = ['mat\n', 'west\n', 'plan\n', 'Good Morning!\n']

# s1 and s2 can be text files
diff = difflib.context_diff(s1, s2)
print(diff)
delta = ''.join(diff)
print(delta)

# set n=0, only output different lines, skip the same lines
diff = difflib.context_diff(s1, s2, n=0)
print(diff)
delta = ''.join(diff)
print(delta)

# The context diff format normally has a header for filenames and modification times.
# Any or all of these may be specified using strings for fromfile, tofile, fromfiledate, and tofiledate
sys.stdout.writelines(difflib.context_diff(s1, s2, fromfile='before.py', tofile='after.py', fromfiledate='Dec. 30 2022', tofiledate='Dec. 30, 2022'))

sys.stdout.writelines(difflib.unified_diff(s1, s2, fromfile='before.py', tofile='after.py', fromfiledate='Dec. 30 2022', tofiledate='Dec. 30, 2022'))

# difflib.get_close_matches
# parameters: (words, possibilities, n=3, cutoff=0.6), words: a sequence for which close matches are desired
# possibilities is a list of sequences against which to match word
# return a list of the best ‘good enough’ matches.

tlist = difflib.get_close_matches('belive', ['live', 'believe', 'achieve', 'inaprpropriate'])
print(tlist)

import keyword
tlist = difflib.get_close_matches('else', keyword.kwlist)
print(tlist)
tlist = difflib.get_close_matches('el', keyword.kwlist)
print(tlist)



# SequenceMatcher object
s = difflib.SequenceMatcher(None, 'abcd', 'abcd abcd')

print(s.find_longest_match(0, 4, 0, 8))

s = difflib.SequenceMatcher(None, 'Liuna', 'Lina')
print(s.ratio())
s = difflib.SequenceMatcher(None, 'Lina', 'Liuna')
print(s.ratio())

s = difflib.SequenceMatcher(None, 'tide', 'diet')
print(s.ratio())
s = difflib.SequenceMatcher(None, 'diet', 'tide')
print(s.ratio())

# Compare Two strings, considering blanks to be 'junk':
s = difflib.SequenceMatcher(lambda x: x == ' ',
                            'However Moreover In addition Therefore',
                            'Therefore However In addition Moreover')
print(s.ratio())
print(round(s.ratio(), 3))

# Differ objects
# compare two texts
# the texts made of sequences of individual single-line strings ending. with newlines

text1 = """1. That's great!
    2. Congratulations.
    3. I'm so glad to hear that!
    4. I'm very happy for you!
    5. Wow! That's awesome!
    6. That's very good news.
    7. Wonderful!
    8. Well done!
""".splitlines(keepends=True)


text2 = """1. That's great!
    2. Awesome!
    3. I'm so glad to hear about that!
    4. I'm really happy for you!
    5. Wow! That's Fantastic!
    6. That's very good news.
    7. Wonderful!
    8. Well done!
""".splitlines(keepends=True)

d = difflib.Differ()
result = d.compare(text1, text2)
pr = ('\n').join(result)
print(pr)

result = list(d.compare(text1, text2))
from pprint import pprint
pprint(result)

import sys
sys.stdout.writelines(result)


str1 = 'BIT_AND'
strlist = ['bit_count','bit_and', 'bitand','bit_or', 'bit_not', 'bit_xor']

def close_match(word, word_list):
    word = word.lower()
    res = difflib.get_close_matches(word, word_list)
    high_r = 0
    high_match_word = str()
    for w in res:
        r = difflib.SequenceMatcher(None, word, w).ratio()
        print(word, w, r)
        if high_r < r:
            high_r = r
            high_match_word = w
    return high_match_word

print(close_match(str1, strlist))
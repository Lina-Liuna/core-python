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

list = difflib.get_close_matches('belive', ['live', 'believe', 'achieve', 'inaprpropriate'])
print(list)

import keyword
list = difflib.get_close_matches('else', keyword.kwlist)
print(list)
list = difflib.get_close_matches('el', keyword.kwlist)
print(list)

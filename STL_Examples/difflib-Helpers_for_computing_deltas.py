# difflib.context_diff(a,b,formfile=‘’,tofile=‘’,fromfiledate=‘’,tofiledate=‘’,n=3, lineterm=‘\n’
# compare a and b(strings) return a delta(a generator generating the delta lines) in context diff format
# returns a delta(a generator generating the delta lines)
import difflib

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
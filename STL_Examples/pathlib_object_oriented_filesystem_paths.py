# pathlib offers classes representing filesystem paths with semantics appropriate for different os.
# path classes are divided between pure paths, which provides purely computational operations without I/O
# and concrete paths, which inherit from pure paths but also provide I/O operations.
# pure paths useful when your code only manipulates paths without actually accessing the OS

from pathlib import Path

# 1. list subdirectorys of . folder
p = Path('.')
p_iterdir = [x for x in p.iterdir() if x.is_dir()]
print(p_iterdir)

# 2. listing Python source files in this directory tree
p = Path('.')
p_l = list(p.glob('*.py'))
print(p_l)

# 3. Navigating inside a directory tree
p = Path('/etc')
q = p / 'init.d' / 'reboot'
print(q)
print(q.resolve())

p = Path('/etc')
q = p / '*.*'
print(q)
print(q.resolve())

p = Path('../')
q = p / 'STL_Examples'
print(q)
print(q.resolve())

# 4. Querying path properties:
print(q.exists(), q.is_dir())


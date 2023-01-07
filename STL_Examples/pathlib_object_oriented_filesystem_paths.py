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

# 5. Opeing a file
p = Path('../')
q = p / 'STL_Examples/pathlib_object_oriented_filesystem_paths.py'

with q.open() as f:
    print(f.readline())

# Pure paths:
# Pure path objects provide path=handling operations which don't actually access a file system.

import os
import pathlib
p = pathlib.PurePath('/etc')
print(os.fspath(p))
print(str(p))
print(p.parts)

p = pathlib.PureWindowsPath('c:/Program Files')
print(str(p))

# Concrete paths
# Concrete paths are subclasses of the pure path classes.
# In addition to operations provided by the latter, they also provided methods to do system calls on path objects.
p = pathlib.Path.cwd()
print(str(p))

p = pathlib.Path.home()
print(str(p))

# Path.stat return os.stat_result
p = pathlib.Path('Built-In_Types.py')
print(p.stat().st_size)

# expanduser()
p = pathlib.Path('~/Booklist')
exp_p = p.expanduser()
print(str(exp_p))

# glob the given relative pattern in the directory represented by this path, yielding all matching files
s_glob_pattern = '*.py'
p = pathlib.Path('.').glob(s_glob_pattern)
print(str(sorted(p)))

# Note: Using the '**' pattern in large directory trees may consume an inordinate amount of time
s_glob_pattern = '**/*.py'
p = pathlib.Path('.').glob(s_glob_pattern)
print(str(sorted(p)))

p = pathlib.Path('.')
p = p.absolute()
print(p)











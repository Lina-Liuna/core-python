# os.path.commonprefix(list)
# return the longest path prefix(taken character-by-character) that is a prefix of all paths in list
import os.path
import pathlib

common_prefix = os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
print(common_prefix)

common_prefix = os.path.commonpath(['/usr/lib', '/usr/local/lib'])
print(common_prefix)

p = pathlib.Path('~/Booklist/README.md')
p = p.expanduser()

split_path = os.path.splitdrive(str(p))
print(split_path)

split_text = os.path.splitext(str(p))
print(split_text)


# os.path.commonprefix(list)
# return the longest path prefix(taken character-by-character) that is a prefix of all paths in list
import os.path

common_prefix = os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
print(common_prefix)

common_prefix = os.path.commonpath(['/usr/lib', '/usr/local/lib'])
print(common_prefix)
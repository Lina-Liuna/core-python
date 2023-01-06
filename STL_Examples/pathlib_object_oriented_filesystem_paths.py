# pathlib offers classes representing filesystem paths with semantics appropriate for different os.
# path classes are divided between pure paths, which provides purely computational operations without I/O
# and concrete paths, which inherit from pure paths but also provide I/O operations.
# pure paths useful when your code only manipulates paths without actually accessing the OS

from pathlib import Path

p = Path('.')
p_iterdir = [x for x in p.iterdir() if x.is_dir()]
print(p_iterdir)
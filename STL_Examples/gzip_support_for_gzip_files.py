import gzip
import shutil
import os.path
import pathlib

# use gzip to compress an existing file.
filename ='README.md'
p = pathlib.Path('~/code/Booklist/' + filename)
p = p.expanduser()
print(p)
print(str(p))
with open(p, 'rb') as f_in:
    with gzip.open(str(p) +'.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
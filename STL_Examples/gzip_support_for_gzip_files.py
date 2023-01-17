import gzip
import shutil
import os.path
import pathlib

# use gzip to compress an existing file.
filename ='temp.db'
p = pathlib.Path('~/code/core-python/STL_Examples/' + filename)
p = p.expanduser()
print(p)
print(str(p))
with open(p, 'rb') as f_in:
    with gzip.open(str(p) +'.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Create a compressed GZIP file
content = b'Miss You'
with gzip.open(str(p) + 'temp.txt.gz', 'wb') as f:
    f.write(content)

# How to read a compression file
with gzip.open(str(p) + 'temp.txt.gz', 'rb') as f:
    print(f.read())
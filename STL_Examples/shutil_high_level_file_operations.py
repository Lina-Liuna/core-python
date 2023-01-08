import shutil
import os
import random
dir = "../"

if os.path.exists(dir + 'odd/'):
    shutil.rmtree(dir + 'odd/')

foldername = '../' + str(random.randint(1, 10_000)) + '/'
print(foldername)

shutil.copytree('../Effective_Python', foldername)
shutil.copy('Built-In_Types.py', foldername)

if os.path.exists( foldername):
    shutil.rmtree(foldername)

print(shutil.which('os'))
print(shutil.which('python'))

# create a gzip'ed tar-file archive containing all files found in the .ssh directory of the user
#archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
archive_name = os.path.expanduser(os.path.join('~', 'code/core-python/STL_Examples/myarchive'))
root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
print(shutil.make_archive(archive_name, 'gztar', root_dir))
os.remove(archive_name+ '.tar.gz')
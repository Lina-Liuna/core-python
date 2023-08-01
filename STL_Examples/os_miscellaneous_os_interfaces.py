# The example displays the number of bytes taken by non-directory files in each directory under the starting directory
# except that it doesn't look under any CSV subdirectory

import os

def count_bytes_size_of_files_in_subdir(dir):
    for root, dirs, files in os.walk(dir):
        print(root, 'consumes', end=' ')
        print(sum(os.path.getsize(os.path.join(root, name)) for name in files), end=' ')
        print(f'bytes in, {len(files)}, non-directory files')
        if 'CSV' in dirs:
            dirs.remove('CSV')

dir = '/Users/linaliu/code/data_analytics/'

count_bytes_size_of_files_in_subdir(dir)

def del_everything_in_dir(dir):
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name))
        for name in dirs:
            os.rmdir(os.path.join(root,name))

if not os.path.exists(dir+'temp'):
    os.makedirs(dir+'temp')

if not os.path.exists(dir+'temp/temp/'):
    os.makedirs(dir+'temp/temp/')

with open(dir+'temp/'+'temp.txt', 'w') as f:
    f.write('hello temp test')

del_everything_in_dir(dir + 'temp')



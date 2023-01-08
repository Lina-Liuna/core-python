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



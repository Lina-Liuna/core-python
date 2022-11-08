
#what we need to know about file/dir operations
#1. os module: us import os instead of from os import *: this will keep os.open() from shadowing the built-in open() function which operate much differently
import os
print(os.getcwd())      #return the current working directory

audiodir = '/Users/kc/books/librarybooks/audlt/audio/'
os.chdir(audiodir)

if not os.path.exists(audiodir + 'today/'):
    os.system('mkdir today')
os.system('rm -rvf today')

#2. built-in dir() and help() functions are useful as interactive aids for working with large modules like os:
import os
#print(dir(os))
#print(help(os))

#3.using shutil module to provides higher level interface for daily file and directory management tasks.
import shutil
os.system('touch today.txt')
shutil.copyfile('today.txt', 'yesterday.txt')
if not os.path.exists(audiodir + 'today/'):
    os.system('mkdir today')
shutil.move('today.txt', audiodir +'/today/')
os.system('rm yesterday.txt')
os.system('rm -rvf today')

# glob module provide a function for making file lists from directory wildcard searches
import glob
print(glob.glob('/Users/kc/code/*/*.py'))

#Command Line Arguments, storeed in sys.argv attributes as a list
import sys
print(sys.argv)

#argparse module provide a more sophisticated mechanism to process cmd line argument.
import argparse
parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')

parser.add_argument('filename', nargs='+')
parser.add_argument('-1', '--lines', type=int, default=10)
#args = parser.parse_args()
#print(args)

#sys module has attributes for stdin, stdout, stderr.
#using stderr to emitting warnings and error messages
sys.stderr.write("warning, log file not found starting a new one")

#most direct way to terminate a script is to use sys.exit()
cnt = 0
while True:
    cnt = cnt + 1
    print("hello world")
    if cnt == 10:
        #sys.exit()
        break


#re module provides regular expression tools for advanced string processing.
import re
print(re.findall(r'\bf[a-z]*', "which foot or hand fell faster"))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print('tea for too'.replace('too', 'two'))
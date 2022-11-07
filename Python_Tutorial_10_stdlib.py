
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



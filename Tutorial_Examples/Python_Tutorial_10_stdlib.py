
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

#use math module to handle floating point math
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))


#use random moudle to making random selections
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())    # random float
print(random.randrange(6)) #random integer chosen from range(6)

#use statistics module to calculate basic statistical properties
#Is there something wrong with the result?
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1,25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

#modules in SciPy project for numerical computations.


#use urllib.request module to retrieving data from URLs
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()     #convert bytes to a string
        if line.startswith('datetime'):
            print(line.rstrip())  #remove trailing newline


#use smtplib module for sending mail
import smtplib
#server = smtplib.SMTP('localhost')      #Why it not worked?
#server.sendmail('liuna.lina@gmail.com', 'liuna.lina@gmail.com',
#                """To: liuna.lina@gmail.com
#                From: liuna.lina@gmail.com
#                Winter time and rainny days
#                """)
#server.quit()

from datetime import date
now = date.today()
print(now)

print(now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B'))

birthday = date(1990, 1, 1)
age = now - birthday
print(age)

#Data Compression
import zlib
s = b'why witch? but wizard of oz wondered which wizard wrist watch'
print(len(s))

t = zlib.compress(s)
len(t)
print(zlib.decompress(t))
print(zlib.crc32(s))

#Performance Measurement
#use timeit module demonstrates a modest performance advantage
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1;b=2').timeit())


#Quality Control: write tests for each function is one approach for developing high quality software.
#use doctest module to scanning a module and validating tests embedded in a program's docstrings.
def average(values):
    return sum(values) / len(values)

import doctest
average([10, 20, 40])
doctest.testmod()

#use unitest module for more comprehensive set of tests
import unittest
class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1,5,7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()



# output formating
# use the reprlib module for abbreviated displays of large or deeply nested cotainers.
# used reprlib for debugging
# reprlib.repr() function returns the object representation in string format.

import reprlib

print(reprlib.repr(set('superherolinasaveherownworld')))

# The pprint module knowns as "pretty printer" that can adds line breaks and more clearly reveal data structure.

import pprint

t = [[[['black', 'cyan'], 'white', ['orange', 'red']], [['blue', 'yellow'], 'pink']]]
pprint.pprint(t, width=40)

# textwrap module formats paragraphs of text to fit a given screen width:

import textwrap

doc = """
The wrap() method is just like fill() except that it returns a list of strings instead of 
one big string with newlines to separate the wrapped lines.
"""
print(textwrap.fill(doc, width=50))

# The locale module accesses a database of culture specific data formats.
# method in locale  module provides a way of formatting numbers with group separator.
import locale

# locale.setlocale(locale.LC_ALL, 'test_file.txt')    #Why error here?
conv = locale.localeconv()
x = 12345678.9
# locale.format("%d", x, grouping=True) #locale.format will be removed in a future version of python
locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)

# 11.2 Templating
# Users can substitute placeholder in Template class in string module
from string import Template

t = Template('${customer} folk send $$10 to $cause')
print(t.substitute(customer='Lina', cause='the donate'))

# substitute method may raise KeyError if placeholder not supplied in a dictionary or a keyword argment
t = Template('Return the $item to $owner')
d = dict(item='w. bush')
# print(t.substitute(d)) # Error

print(t.safe_substitute(d))

# Template subclasses can specify a custom delimiter
import time, os.path
from PIL import Image
from pathlib import Path


dir = '/Users/kc/books/raz-kids/bypython/'
pic_ext = '.jpg'


def get_image_list(image_list, dir):
    os.chdir(dir)
    paths = sorted(Path(dir).iterdir(), key=os.path.getmtime)
    for img in paths:
        basename = os.path.basename(img)
        dirname = os.path.dirname(img)
        if pic_ext not in basename:
            continue
        image_list.append(basename)


photo_files = []
get_image_list(photo_files, dir)


class BatchRename(Template):
    delimiter = '%'


fmt = input('Enter rename style (%d-date %n-seqnum %f-format):')

# AMAZING AMAZING
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photo_files):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


# How to loop through header information in a zip file without using zipfile module by
# using pack() and unpack() functions in struct module
import struct

with open('/Users/kc/code/core-python/test_file.txt.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    # H and I represent two and four byte unsigned numbers respectively
    # < indicate that they are standard size and in little-endian byte order.
   # fields = struct.unpack('<IIIHH', data[start:start+16])
   # crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

   # start += 16
   # filename = data[start:start+filenamesize]
  #  start += filenamesize
  #  extra = data[start:start+extra_size]
   # print(filename, hex(crc32), comp_size, uncomp_size)

  #  start += extra_size + comp_size


# use threading module for multi-threading, can run tasks in background while the main program continues to run
# what the challenge of the multi-threaded application:
# 1. coordinating threads that share data or other resources, including locks, event, condition  variables, semahpores
# 2. how to coordinate resources between tasks?
# concentrate all access to a resource in a single thread and then use queue module to feed that thread with request from other thread.

import threading, zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile


    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

dir ='/Users/kc/code/core-python/'
background = AsyncZip(dir + 'test_file.txt', dir + 'mytar.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()      # wait for the background task to finish
print('Main program waited until background was done.')


import logging
logging.debug('Debugging Info')
logging.info('Information msg')
logging.warning('Warning: config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# weakref module
# python does automatic memory management, the memory is freed shortly after the last reference to it has been eliminated.
# what if we want to track objects? just tracking them creates a reference that makes them permanent.
# weakref module provides tools for tracking objects without creating a reference.

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])

del a
gc.collect()


# array.arry() stores only homogeneous data and stores it more compactly.
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

# coolections.deque() with faster appends and pops from the left side but slower loopups in the middle.
from collections import deque
d = deque(['t1', 't2', 't3'])
d.append('t4')
print('handling', d.popleft())

# collections.deque are well suited for implementing queues and breath first tree searches
unsearched = deque(['t1', 't2', 't3', 't4'])
def breath_first_search(unsearched):
    node = unsearched.popleft()
    #for m in gen_moves(nodes)
    #???????????????????

# bisect module for manipulating sorted list.
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]

bisect.insort(scores, (300, 'ruby'))
print(scores)


# heapq module for implementing heaps based on regular lists, th valued entry is always kept at position zero.
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(heapify(data))
print(data)

heappush(data, -5)
print([heappop(data) for i in range(3)])















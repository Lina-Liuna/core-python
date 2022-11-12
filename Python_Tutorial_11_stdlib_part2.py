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


dir = '/Users/ln/books/raz-kids/bypython/'
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


fmt = input('Enter rename style (%d-date %n-seqnum %%f-format):')


t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photo_files):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

# output formating
# use the reprlib module for abbreviated displays of large or deeply nested cotaners.
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
#locale.setlocale(locale.LC_ALL, 'test_file.txt')    #Why error here?
conv = locale.localeconv()
x = 12345678.9
locale.format("%d", x, grouping=True)
locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)
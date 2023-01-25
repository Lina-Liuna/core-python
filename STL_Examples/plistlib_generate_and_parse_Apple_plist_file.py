# plist module: provide an interface for reading and writing the "property list" files used by Apple.
# This module supports both binary and XML plist files.

# The property list(.plist) file format is a simple serialization supporting basic object types, like dictionaries,
# lists, numbers and strings.

# To write out and parse a plist file, use the dump() and load() functions
# To work with plist data in bytes objects, use dumps() and loads() functions
import plistlib
import datetime
import time

def generate_plist_file(filename):
    pl = dict(
        aString="Doodah",
        aList=["A", "B", 12, 32.1, [1, 2, 3]],
        aFloat=0.1,
        anInt=728,
        aDict=dict(
            anotherString="<hello & hi there!>",
            aThirdString="M\xe4ssig, Ma\xdf",
            aTrueValue=True,
            aFalseValue=False,
        ),
        someData=b"<binary gunk>",
        someMoreData=b"<lots of binary gunk>" * 10,
        aDate=datetime.datetime.fromtimestamp(time.mktime(time.gmtime())),
    )
    with open(filename, 'wb') as fp:
        plistlib.dump(pl, fp)

def parsing_plist_file(filename):
    with open(filename, 'rb') as fp:
        pl = plistlib.load(fp)
    print(pl)
    print(pl["aDate"])

dir = '/Users/linaliu/code/core-python/STL_Examples/'
generate_plist_file(dir + 'temp.plist')
parsing_plist_file(dir + 'temp.plist')


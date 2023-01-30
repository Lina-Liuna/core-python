# The time module provides various time-related functions.
# For related functionality, see also the datetime and calendar modules
# Most of the functions defined in this module call platform C library functions with the same name.

import collections
import time
import os

time_directives = collections.defaultdict(str)
time_directives = {
    '%a' : 'Locale\'s abbreviated weekday name',
    '%A' : 'Locale\'s full weekday name',
    '%b' : 'Locale\'s abbreviated month name',
    '%B' : 'Locale\'s full month name',
    '%c' : 'Locale\'s appropriate date and time representation',
    '%d' : 'Locale\'s Day of the month as a decimal number',
    '%m' : 'Month as decimal number',
    '%M' : 'Minute as a decimal number [00,59].',
    '%H' : 'Hour (24-hour clock) as a decimal number [00,23].',
    '%Y' : 'Year without century as a decimal number [00,99].',
    '%y' : 'Year with century as a decimal number.',

}

print(list(time_directives.keys()))

s = ','.join(list(time_directives.keys()))
print(time.strftime(s,time.gmtime()))

s = '%a %b %d %H:%M:%S %Y'
print(time.strptime('30 Jan 23', '%d %b %y'))





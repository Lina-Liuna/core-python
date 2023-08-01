# urllib.parse used to break URL(Uniform Resource Locator) strings up in components(addressing scheme,
# network location, path etc.)
#
# urllib.parse used to combine the components back into a URL string,
#
# urllib.parse used to convert a relative URL to an absolute URL given a base URL

# urllib.parse support URL schemes: file, ftp, gopher,
# hdl, http, https, imap, mailto, mms, news, nntp, prospero, rsync, rtsp, rtspu, sftp, shttp, sip, sips, snews, svn,
# svn+ssh, telnet, wais, ws, wss.

# urllib.parse module defines functions that fall into two broad categories: url parsing and url quoting.

# urllib.parse focus on splitting a URL string into its components,
# urllib.parse focus on combining URL components into a URL string.


# what does parse_qs do?
# parse a query string given as a  string argument. data returned as a dictionary.
# the dictionary keys are the unique query variable names
# the dictionary values are the lists of values for each name.
from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
# repr() functions return a printable representation of the given object
print(repr(my_values))
print(my_values)

print('red ', my_values.get('red'))
print('green ', my_values.get('green'))
# will print 'None'
print('opacity ', my_values.get('opacity'))

# how to solve the empty string None, the empty list? the zero value? not to be none?
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print(f'red: {red!r}')
print(f'green: {green!r}')
print(f'opacity:{opacity!r}')

# The above is a little hard to read. use if else keeping the code short
red_str = my_values.get('red', [''])
red = int(red_str[0]) if red_str[0] else 0

# but the repeat of red green opacity made it more complicated.

# solution: write a helper function to reuse the logic repeatly

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opacity = get_first_int(my_values, 'opacity')
print(red, green, opacity)




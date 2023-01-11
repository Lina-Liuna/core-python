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

from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
# repr() functions return a printable representation of the given object
print(repr(my_values))
print(my_values)

print('red ', my_values.get('red'))
print('green ', my_values.get('green'))
print('opacity ', my_values.get('opacity'))
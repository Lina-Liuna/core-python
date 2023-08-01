# the blob find all the pathnames matching a specified pattern

import glob

l = glob.glob('[0-9].*')
print(l)

# output all files under current directory
l = glob.glob('*.*')
print(l)

print(help(glob.glob))
l = glob.glob('*.*')
print(l)
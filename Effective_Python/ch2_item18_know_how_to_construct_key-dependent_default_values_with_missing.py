# there are times when neither setdefault nor defaultdict is the right fit.
# Example: writing a program to manage social network profile pictures on the filesystem.
# I need a dictionary to map profile picture pathnames to open file handles
# so I can read and write those images as needed.

# The prefect solution is: subclass the dict type and implement the __missing__ special method to add custom logic
# for handling missing keys.

import collections

def open_pictures(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'Failed to open path {profile_path}')
        raise


class Pictures(dict):
    def __missing__(self, key):       # __missing_method create the new default value for the keys, insert it into dict.
        value = open_pictures(key)
        self[key] = value
        return value

dir = '/Users/linaliu/books/fonts/generate/sightwordslevel1/'
png_name = '2a and are can do go he she is like.png'
path = dir + png_name
pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
print(image_data)

dir = '/Users/linaliu/books/fonts/generate/sightwordslevel1/'
png_name = 'new fakefakefake.png'
path = dir + png_name
pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
print(image_data)

# Things to remember:
# the setdefault method of dict is a bad fit when creating the default value has high computational cost or
# may raise exceptions.

# The function passed to defaultdict must be not require any arguments, which makes it impossible to have he default
# value depend on the key being accessed.

# You can define your own dict subclass with a __missing__ method in order to construct default values that must know
# which key was being accessed.
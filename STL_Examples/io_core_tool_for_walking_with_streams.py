# The io module provides pythons' main facilities for dealing with various types of I/O
# There are three main types of I/O: text I/O, binary I/O, and raw I/O.
import io


def read_png_file(filename):
    with io.open(filename, 'rb', buffering=0) as f:
        print(f.readable())
        print(f.readlines())

dir = '/Users/linaliu/books/fonts/generate/sightwordslevel1/'
png_name = '2a and are can do go he she is like.png'
read_png_file(dir+png_name)
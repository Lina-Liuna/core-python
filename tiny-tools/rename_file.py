import os
import sys
from pathlib import Path

listdir = sys.argv[1]
print("Command-line Arguments:",listdir)

ext = '.crdownload'

def getnewname(filename):
    return '.'.join(filename.split('.')[:-1])

def change_file_name(filename):
    basename = os.path.basename(filename)
    dir = os.path.dirname(filename)

    if ext not in basename:
        return filename
    newfilename = dir + '/' + getnewname(basename)
    print(newfilename)
    os.rename(filename, newfilename)

def rename_sorted_file(dir):
    os.chdir(dir)
    paths = sorted(Path(dir).iterdir(), key=os.path.getmtime)

    for file_name in paths:
        #print(file_name)
        change_file_name(file_name )

rename_sorted_file(listdir)
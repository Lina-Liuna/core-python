from filecmp import dircmp
import pathlib

def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print('diff_file %s found in %s and %s' %(name, dcmp.left, dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

p = pathlib.Path('~/code/Booklist')
exp_p = p.expanduser()
dir1 = str(exp_p)

p = pathlib.Path('~/code/core-python')
exp_p = p.expanduser()
dir2 = str(exp_p)

dcmp = dircmp(dir1, dir2)
print_diff_files(dcmp)
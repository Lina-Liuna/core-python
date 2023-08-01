# The argparse module makes it easy to write user-friendly cmd-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# the argparse module also automatically generates help and usage messages.

import argparse

# Step1: using the argparse to creating an ArgumentParser object
# parser = argparse.ArgumentParser(description='Process some integers.')

# Step2: Fill the ArgumentParser with information about program arguments is done by making calls to the add_argument
# parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate',action='store_const', const=sum, default=max, help='sum the integers')

# Step3: call parse_args to inspect the command line, convertt each argument to the appropriate type and invoke the appropriate action.
# args = parser.parse_args()
# print(args.accumulate(args.integers))


# Sometimes, when dealing with a particularly long argument list, it may make sense to keep the list of arguments in a file
# rather than typing it out at the cmd line.

# If the fromfile_prefix_chars= argument is given to the ArgumentParser constructor, then arguments that start with any
# of the specified characters will be treated as files, and will be replacd by the arguments they contain.

def parse_cmd_line_in_file(filename):
    with open(filename, 'w') as fp:
        fp.write('-f\nbar')
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument('-f')
    parser.parse_args(['-f', 'foo', '@args.txt'])

dir = '/Users/linaliu/code/core-python/STL_Examples/'
# parse_cmd_line_in_file(dir+'args.txt')

def parse_cmd_line():
    parser = argparse.ArgumentParser(description='Data Type and Function mapping ')
    parser.add_argument('-dtm', metavar='--data-type-mapping', type=bool, action='store',help='display data type mapping')
    parser.add_argument('-fm', metavar='--func-mapping', type=bool, action='store', help='display function mapping')
    parser.add_argument('-sm', metavar='--single-mapping', type=str, action='store', help='display a single mapping')
    parser.add_argument('-o', metavar='--output', type=str, action='store', help='output all the displays into a file')
    args = parser.parse_args()
    print(args)
    print(args.dtm)
    print(args.fm)
    print(args.sm)
    print(args.o)

parse_cmd_line()
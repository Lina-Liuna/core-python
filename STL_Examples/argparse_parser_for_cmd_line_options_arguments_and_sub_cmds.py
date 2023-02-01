# The argparse module makes it easy to write user-friendly cmd-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# the argparse module also automatically generates help and usage messages.

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate',action='store_const', const=sum, default=max, help='sum the integers')
args = parser.parse_args()
print(args.accumulate(args.integers))
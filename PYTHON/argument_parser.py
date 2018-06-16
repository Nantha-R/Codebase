# Argument parser is used for parsing the command line arguments

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('-a', '--arg1', dest='arg1', required=True)
# results in an error if the above mentioned argument is not present
parser.add_argument('-b', '--arg2', dest='arg2', default='abc')
# Assigns a default value to the variable if not given in the arguments
# Retrieving the arguments from the parser object
args = parser.parse_args()
argument_one = args.arg1
argument_two = args.arg2

# https://pymotw.com/2/argparse/

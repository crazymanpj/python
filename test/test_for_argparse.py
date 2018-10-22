import argparse

parser = argparse.ArgumentParser(description='test')
parser.add_argument('echo')
# parser.add_argument("-v", "--verbosity", help='test verbosity')
parser.add_argument("-t", "--test", help='test something', action="store_true")
args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")

if args.test:
    print('test turned on')

import sys
import pygreppy
from pygreppy import Args, parse, usage

def main():
    args = Args(sys.argv[1:])
    if args.args == 1:
        usage()
        sys.exit(1)
    else:
        print('\n' + parse(args))


if __name__ == '__main__':
    main()

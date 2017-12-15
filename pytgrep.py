#!/usr/bin/env python
import sys
import os

class Args:

    def __init__(self, args):
        self.context = False
        self.cl = False
        self.func = False
        self.depth = 0
        self.path = None
        self.pattern = None
        self.args = self.parseargs(args)

    def parseargs(self, args):
        print(args)
        for arg in args:
            if arg == '-cl':
                self.cl = True
                args.remove(arg)
            elif arg == '-c':
                if arg != args[-1] and args[args.index(arg)+1].isdigit():
                    self.depth = int(args[args.index(arg)+1])
                    args.remove(args[args.index(arg)+1])
                else:
                    self.depth = 1
                args.remove(arg)
            elif arg == '-f':
                self.func = True
                args.remove(arg)
        if not os.path.exists(args[-1]):
            print('Error: no file {}'.format(args[-1]))
            return 1
        elif not args[-1].endswith('.py'):
            with open(args[-1]) as f:
                line = f.readline(0)
                if not '#!' in line and not 'python' in line:
                    print('Error: {} is not a python script'.format(args[-1]))
                    return 1
        self.path = args[-1]
        args.remove(args[-1])
        if len(args) != 0:
            self.pattern = args[-1]
            args.remove(args[-1])
        else:
            print('Error: there is no search pattern')
            return 1
        if len(args) != 0:
            print('USAGE!')
            return 1
        return 0

def main():
    args = Args(sys.argv[1:])
    if args.args == 1:
        print('USAGE')
        sys.exit(1)
    else:
        print(args.args)
        print('LETS GO!')


if __name__ == '__main__':
    main()

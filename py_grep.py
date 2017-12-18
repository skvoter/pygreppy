#!/usr/bin/env python
from pygments.lexers.python import PythonLexer
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
import shutil
import ast
import codegen
import sys
import os


def usage():
    print('''
usage: pytgrep [-c <depth> | -cl | -f] (optional) pattern file

file should be python script formatted with pep8 guidelines

optional arguments:
-h          show this page
-c [depth]  show context of the string.
-cl         show class containing string (ignored if no class)
-f          show function containing string (ignored if no function)

Note: only one option can be specified at a time.
''')


def get_numlines(node):
    return len(codegen.to_source(node).split('\n'))


def mhighlight(num, string, pattern):
    if pattern == '':
        return ('\033[1;90m{:0>2}\033[0;0m'.format(
            num,
            highlight(
                string.split(pattern)[0],
                PythonLexer(),
                TerminalFormatter()).strip('\n'),
            ))
    else:
        return ('\033[1;90m{:0>2}\033[0;0m {}\033[1;91m{}\033[0;0m{}'.format(
            num,
            highlight(
                string.split(pattern)[0],
                PythonLexer(),
                TerminalFormatter()).strip('\n'),
            pattern.strip('\n'),
            highlight(
                string.split(pattern)[1],
                PythonLexer(),
                TerminalFormatter()).lstrip('\n')
            ))


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
        for arg in args:
            arg = args[0]
            if arg == '-cl':
                self.cl = True
                args.remove(arg)
            elif arg == '-h':
                return 1
            elif arg == '-c':
                self.context = True
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
                if '#!' not in line and 'python' not in line:
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
            for arg in args:
                print('{} is not recognized option'.format(arg))
            return 1
        if len(
            [arg for arg in [self.cl, self.func, self.context] if arg is True]
        ) > 1:
            print('Error: Only one of -cl, -c, -f can be used at a time')
            return 1
        return 0


def find_match_node(results, num, root, args):
    for node in ast.walk(root):
        for child in ast.iter_child_nodes(node):
            if args.pattern in codegen.to_source(child) and \
               hasattr(child, 'lineno') and \
               child.lineno == num:
                return child


def get_end(node):
    ints = []
    for child in ast.walk(node):
        for ch in ast.iter_child_nodes(node):
            if hasattr(ch, 'lineno'):
                ints.append(ch.lineno)
    return max(ints)


def context_parse(args):
    with open(args.path) as f:
        content = f.read()
    results = []
    root = ast.parse(content)
    for node in ast.walk(root):
        for child in ast.iter_child_nodes(node):
            child.parent = node
    # search for pattern
    for num, line in enumerate(content.split('\n'), 1):
        if args.pattern in line and line not in [
            item for sublist in [
                it.split('\n') for it in results
            ] for item in sublist
        ]:
            pattern_node = find_match_node(results, num, root, args)
            top_root = False
            if pattern_node.parent is root:
                top_root = True
            else:
                for i in range(args.depth):
                    pattern_node = pattern_node.parent
                    if pattern_node.parent is root:
                        top_root = True
                        break
            first = pattern_node.lineno
            end = get_end(pattern_node)
            if top_root is True:
                if pattern_node is not root.body[0]:
                    top = root.body[root.body.index(pattern_node)-1]
                # if pattern_node


def parse(args):
    results = []
    if args.context:
        results = context_parse(args)
    else:
        with open(args.path) as f:
            ln = 0
            curres = ''
            for num, line in enumerate(f, 1):
                if args.pattern in line:
                    a = mhighlight(num, line, args.pattern)
                    if num == ln + 1:
                        curres += a
                    else:
                        results.append(curres)
                        curres = a
                    ln = num
            results.append(curres)
    return ('\n\033[1;90m'
            + '='*shutil.get_terminal_size()[0]
            + '\033[0;0m\n\n').join(results)


def main():
    args = Args(sys.argv[1:])
    if args.args == 1:
        usage()
        sys.exit(1)
    else:
        print(parse(args))


if __name__ == '__main__':
    main()

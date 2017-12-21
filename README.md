# pygreppy [![Build Status](https://travis-ci.org/skvoter/pygreppy.svg?branch=master)](https://travis-ci.org/skvoter/pygreppy) [![PyPI version](https://badge.fury.io/py/pygreppy.svg)](https://badge.fury.io/py/pygreppy)
Tool for searching in python source code files that supports context output.

Context searching is available with `ast` module and [CensoredUsername](https://github.com/CensoredUsername/)'s [fork](https://github.com/CensoredUsername/codegen) of `codegen` by Armin Ronacher.

## Requirements:
- Python 3.x

## Installation:
`pip install pygreppy`

## Usage:
```
pygreppy [-c <depth> | cl | func] (optional) pattern file

file should be python script (better if formatted with pep8 guidelines)

optional arguments:
-h          show this page
-c [depth]  show context of the string.
-cl         show class containing string (ignored if no class)
-f          show function containing string (ignored if no function)

Note: only one option can be specified at a time.
```

# pygreppy [![Build Status](https://travis-ci.org/skvoter/pygreppy.svg?branch=master)](https://travis-ci.org/skvoter/pygreppy) [![PyPI version](https://badge.fury.io/py/pygreppy.svg)](https://badge.fury.io/py/pygreppy)

Tool for searching in python source code files that supports context output.
![workflow gif](https://i.imgur.com/xmurVnR.gif)

Context searching is available with `ast` module and [CensoredUsername](https://github.com/CensoredUsername/)'s [fork](https://github.com/CensoredUsername/codegen) of `codegen` by Armin Ronacher.

## Requirements:
- Python 3.x

## Installation:
`pip install pygreppy`

## Usage:
`pygreppy [-re | -c <depth> | -cl | -f | -h] (optional) pattern file`

File should be python script (better if formatted with pep8 guidelines)

Optional arguments:

 * **-h**          show usage
 * **-c** [depth]  show context of the string.

 * **-cl**         show class containing string (ignored if no class)

 * **-f**          show function containing string (ignored if no function)

 * **-re**         search pattern is regexp

Note: only one option (except -re) can be specified at a time.

**Example**: `pygreppy -re -f 'myfunction_\d{1}' mynumberedfunctions.py`
This will show all the function named or containing string matching this regexp

## Contibuting
If you wish to contribute - you're welcome!

There are some issues where help is needed or appreciated.

Feature requests are also prefered to be done through the github issues.

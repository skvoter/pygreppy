# pygreppy
Tool for searching in python source code files that supports context output.

Context searching is available with `ast` moldule and [CensoredUsername](https://github.com/CensoredUsername/)'s [fork](https://github.com/CensoredUsername/codegen) of `codegen` by Armin Ronacher.

## Requirements:
- Python 3.x
- [this `codegen` fork](https://github.com/CensoredUsername/codegen)
- `pygments`

## Installation:
`pip install --process-dependency-links pygreppy`

## Usage:
```
pygreppy [-c <depth>] (optional) pattern file

file should be python script (better if formatted with pep8 guidelines)

optional arguments:
-h          show this page
-c [depth]  show context of the string.
# soon will be added
-cl         show class containing string (ignored if no class)
-f          show function containing string (ignored if no function)

Note: only one option can be specified at a time.
```

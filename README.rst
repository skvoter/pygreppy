py-grep
=======

Tool for searching in python source code files that supports context
output.

Context searching is available with ``ast`` moldule and
`CensoredUsername <https://github.com/CensoredUsername/>`__\ ’s
`fork <https://github.com/CensoredUsername/codegen>`__ of ``codegen`` by
Armin Ronacher.

Requirements:
-------------

-  `this ``codegen``
   fork <https://github.com/CensoredUsername/codegen>`__
-  ``pygments`` ## Installation: > Soon it will be available on pip (as
   py_grep)

Usage:
------

::

    pygrep [-c <depth> | -cl | -f] (optional) pattern file

    file should be python script (better if formatted with pep8 guidelines)

    optional arguments:
    -h          show this page
    -c [depth]  show context of the string.
    -cl         show class containing string (ignored if no class)
    -f          show function containing string (ignored if no function)

    Note: only one option can be specified at a time.

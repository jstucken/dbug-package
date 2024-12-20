# dbug-package
Jono's custom Python debugging script.

Similar to but a bit more fancy than using Python's inbuilt `pprint` library to debug/print out your Python variables.

Does a nice job of printing out strings, dictionaries, dataframes, JSON etc.

Note: This is not a true Python debugger in any way, more just a fancy print out class!

# Installation

**Install using pip:**

    pip install dbug-package@git+ssh://git@github.com/jstucken/dbug-package

Or add the following to your `requirements.txt`:

    dbug-package @ git+ssh://git@github.com/jstucken/dbug-package

**Add to an existing [Poetry](https://python-poetry.org/) project:**

    poetry add git+https://git@github.com/jstucken/dbug-package.git

Or manually add the following to your `pyproject.toml` file:

    [tool.poetry.dependencies]
    dbug-package = { git = "https://git@github.com/jstucken/dbug-package.git" }

# Usage

Import and call within your script like this:

    from dbug_package.dbug import Dbug as dbug

    # an example list
    names = ['bill', 'mary']

    dbug(names, "A list of names")

Which will print out something like:

    1) ###########################################################
    [12:23:05] DEBUG    DBUGGING 'A list of names' <class 'list'> (len: 2) in test.py line 6:

    ['bill', 'mary']

# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dbug_package']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=1.0.0,<2.0.0', 'rich>=13.3.3,<14.0.0', 'typer>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'dbug-package',
    'version': '0.1.0',
    'description': 'A minimal debug package for printing out things nicely',
    'long_description': '# dbug-package\nJono\'s custom Python debugging script.\n\nSimilar to but a bit more fancy than using Python\'s inbuilt `pprint` library to debug/print out your Python variables.\n\nDoes a nice job of printing out strings, dictionaries, dataframes, JSON etc.\n\nNote: This is not a true Python debugger in any way, more just a fancy print out class!\n\n# Installation\n\n**Install using pip:**\n\n    pip install dbug-package@git+ssh://git@github.com/jstucken/dbug-package\n\nOr add the following to your `requirements.txt`:\n\n    dbug-package @ git+ssh://git@github.com/jstucken/dbug-package\n\n**Install using [Poetry](https://python-poetry.org/):**\n\n    poetry add git+ssh://git@github.com/jstucken/dbug-package.git\n    poetry update\n\nOr manually add the following to your `pyproject.toml` file:\n\n    [tool.poetry.dependencies]\n    dbug-package = { git = "ssh://git@github.com/jstucken/dbug-package.git" }\n\n# Usage\n\nImport with:\n\n    from dbug_package.dbug import Dbug as dbug\n\nThen call within your script like this:\n\n    # an example list\n    names = [\'bill\', \'mary\']\n\n    dbug(names, "A list of names")\n\nWhich will print out something like:\n\n    1) ###########################################################\n    [12:23:05] DEBUG    DBUGGING \'A list of names\' <class \'list\'> (len: 2) in test.py line 6:\n\n    [\'bill\', \'mary\']',
    'author': 'Jonathan Stucken',
    'author_email': 'jstucken@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

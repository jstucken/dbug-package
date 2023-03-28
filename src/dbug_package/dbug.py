# Python debugging class
# Useful in debugging simple arrays, nested arrays, pandas dataframes
# nested (2d-3d) dictionaries and nested lists
# this script is work in progress
#
# Call the class from your main script like this:
# boats = ["sailing yacht", "kayak"]
# debug(boats, 'a collection of boats')
#
# usage:
# from dbug import Dbug as dbug
#
# Author: jstucken 22-08-2022
import os
import inspect
import logging

import typer
from dotenv import load_dotenv
from rich import print
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table

console = Console()

# configure rich logging
FORMAT = "%(message)s"
logging.basicConfig(
    level="DEBUG",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

# track version number of this dbug script
DBUG_VERSION = 1.1

# track how many times dbug() gets called in a script. This is useful
# for following code flow when debugging
dbug_env_file = "dbug.env"


def env_write(name, value):
    """Sets an environment variable"""
    file = open(dbug_env_file, "w")
    file.write(f"{name}={value}")
    file.close()


def env_read(name):
    """Gets an environment variable"""
    load_dotenv(dbug_env_file, override=True)
    value = os.environ.get("dbug_count")
    return value


def increment_dbug_count():
    """Adds 1 to our dbug_count var"""
    old_value = env_read("dbug_count")
    env_write("dbug_count", int(old_value) + 1)


def get_dbug_count():
    """Gets the current dbug_count from env"""
    return env_read("dbug_count")


# only run this once the first time the dbug class gets imported
env_write("dbug_count", 0)


class Dbug:

    # our dbug method used to debug variables, dictionaries, lists etc
    def __init__(self, data, label: str = None, raw_mode: bool = False):

        increment_dbug_count()

        # gets line info about scripts which called this function etc.
        # Uses the 'inspect' library
        # From which, we need the script name and line number
        # ignore the first two entries as these relate to this dbug class
        ignore_buffer = 2

        line_info_all = self.get_line_info()
        line_info = line_info_all[ignore_buffer]

        filename = line_info.filename
        lineno = line_info.lineno

        spacer = f" {get_dbug_count()}) ########################################################### "
        typer.secho(spacer, fg=typer.colors.WHITE, bg=typer.colors.RED)

        # avoid error when debugging bool, PosixPath etc
        object_length = ""
        if hasattr(data, "__len__"):
            object_length = f"(len: {len(data)}) "

        if label:
            logging.debug(
                f"DBUGGING '{str(label)}' {type(data)} {object_length}in {filename} line {str(lineno)}:\n"
            )
        else:
            logging.debug(
                f"DBUGGING {type(data)} {object_length}{filename} line {str(lineno)}:\n"
            )
        print(data)

    # used for getting traceback line number etc in dbug function()
    def get_line_info(self):

        # returns a big class of frameinfo
        return inspect.stack()

import argparse
from datetime import datetime
import logging
import importlib.util
import os

PROCEDURES = {}


def add_procedure(name, procedure):
    """
    Adds a procedure decorator

    :param name: Decorator name
    :param procedure: Procedure function
    :return: Adds a key (name) and value function (procedure) to the PROCEDURES dict
    """
    PROCEDURES[name] = procedure


def iterative_importer(path):
    """
    Imports every python script from a given path
    Ignores hidden files, files that begin with "." and "_" are considered hidden

    :param path: Path to modules
    :return: Imported modules
    """

    check_hidden = lambda x: x.startswith("_") or x.startswith(".")
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not check_hidden(d)]

        for script in files:
            if not check_hidden(script) and script.endswith(".py"):
                spec = importlib.util.spec_from_file_location(
                    script.rstrip(".py"), os.path.join(root, script)
                )
                spec.loader.exec_module(importlib.util.module_from_spec(spec))


def initialise():
    """
    Return the procedures dict and corresponding functions

    :return: App context
    """
    iterative_importer("quality_checks")
    return PROCEDURES


def configure_parser():
    """
    Arg parser configuration.
    --test: Defaults to False; runs unittests if True.
    :return: args parser
    """
    parser = argparse.ArgumentParser()

    def str_to_bool(value):
        if isinstance(value, bool):
            return value
        if value.lower() in ("yes", "true", "t", "y", "1"):
            return True
        elif value.lower() in ("no", "false", "f", "n", "0"):
            return False
        else:
            raise argparse.ArgumentTypeError("Boolean value expected.")

    parser.add_argument(
        "--test",
        type=str_to_bool,
        nargs="?",
        const=True,
        default=False,
        help="run in test mode (default: False)",
    )
    args = parser.parse_args()
    return args


def configure_logger(args):
    """
    Configures and creates a logger.

    :param args: Log file name
    :return: Logger
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s  |  %(levelname)s  ->  %(message)s")

    msg = "run"
    if args.test:
        msg = "test"

    file_handler = logging.FileHandler(
        f'reports/run_{msg}_{datetime.now().strftime("%Y-%m-%d_%H.%M")}.log'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    return logger.addHandler(file_handler)

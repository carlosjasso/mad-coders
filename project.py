from argparse import ArgumentParser, Namespace, _SubParsersAction
from enum import Enum, auto
from importlib.util import find_spec
from os import getcwd
from os.path import exists
from shutil import rmtree
from subprocess import run
from sys import argv, executable, exit, version_info
from typing import TYPE_CHECKING, Any

SubparsersType = _SubParsersAction[ArgumentParser] if TYPE_CHECKING else Any

required_version_major = 3
required_version_minor = 6


class __parsers(Enum):
    setup = auto()


def main() -> None:
    __validate_runtime_version()
    parser = __init_parser()

    if (len(argv) == 1):
        parser.print_help()
        exit(0)

    args = parser.parse_args()
    subparser = getattr(args, "parser")

    if (subparser == __parsers.setup):
        __handle_setup_parser(args, parser)


def __validate_runtime_version() -> None:
    runtime_version = (version_info.major, version_info.minor)
    required_version = (required_version_major, required_version_minor)
    if (runtime_version < required_version):
        exit(f"{__file__} requires python version {required_version_major}.{required_version_minor}+")


def __init_parser() -> ArgumentParser:
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(
        title="Options",
        required=True
    )

    __add_setup_parser(subparsers)

    return parser


def __add_setup_parser(subparsers: SubparsersType) -> None:
    help_text = "Helps setup different aspects of the project"

    parser = subparsers.add_parser(
        "setup", help=help_text, description=help_text)

    parser.set_defaults(parser=__parsers.setup)

    parser_group = parser.add_mutually_exclusive_group()

    parser_group.add_argument("-e", "--venv", action="store_true",
                              help="Generate a venv directory (installs venv module, if needed).")


def __handle_setup_parser(args: Namespace, parser: ArgumentParser):
    if (getattr(args, "venv")):
        __handle_setup_venv()
    else:
        parser.parse_args(["setup", "--help"])


def __handle_setup_venv():
    if (getcwd() in executable):
        print("venv already setup")
        exit(0)

    if (exists("./.venv/")):
        rmtree("./.venv/")

    __execute_script("pip install venv --upgrade")
    __execute_script("venv .venv")


def __execute_script(script: str) -> None:
    commands = [executable, "-m"] + script.split(" ")
    run(commands)


if (__name__ == "__main__"):
    main()

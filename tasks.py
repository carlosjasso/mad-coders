import sys
import typing
from dataclasses import dataclass
from argparse import ArgumentParser, _SubParsersAction, Namespace

import pelicanconf
import conf

SubparsersType = _SubParsersAction[ArgumentParser] if typing.TYPE_CHECKING else typing.Any

REQUIRED_PYTHON_VERSION_MAJOR = 3
REQUIRED_PYTHON_VERSION_MINOR = 7


@dataclass
class ParserArg:
    ARG: str
    ALT_ARG: str
    DEST: str
    HELP: str
    DEFAULT: typing.Any


@dataclass
class Terms:
    @dataclass
    class MainParser:
        @dataclass
        class IsProd(ParserArg):
            ARG = "--is-prod"
            DEST = "IsProd"
            HELP = "Include it to specify that commands must be executed for production"
            DEFAULT = False

        @dataclass
        class Generate(ParserArg):
            ARG = "-g"
            ALT_ARG = "--generate"
            DEST = "Generate"
            HELP = "Generate the site content"
            DEFAULT = False

    @dataclass
    class ArgparseActions:
        STORE_TRUE = "store_true"


class TasksConfiguration:
    def __init__(self, namespace: Namespace) -> None:
        self.__namespace = namespace

    def __get_value(self, arg: ParserArg) -> typing.Any:
        return getattr(self.__namespace, arg.DEST, arg.DEFAULT)

    @property
    def IsProd(self) -> bool:
        return self.__get_value(Terms.MainParser.IsProd)

    @property
    def IsGenerate(self) -> bool:
        return self.__get_value(Terms.MainParser.Generate)


def main():
    __validate_python_version()
    parser = __build_parser()

    if (len(sys.argv) == 1):
        parser.print_help()
        exit()

    tasksConf = TasksConfiguration(parser.parse_args())

    if (tasksConf.IsGenerate):
        __generate(tasksConf.IsProd)


def __validate_python_version() -> None:
    installed = (sys.version_info.major, sys.version_info.minor)
    required = (REQUIRED_PYTHON_VERSION_MAJOR, REQUIRED_PYTHON_VERSION_MINOR)
    if (installed < required):
        exit(f"{__file__} requires python version {REQUIRED_PYTHON_VERSION_MAJOR}.{REQUIRED_PYTHON_VERSION_MINOR}+ ro tun.")


def __build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Helps with automated tasks of the project."
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        Terms.MainParser.Generate.ARG, Terms.MainParser.Generate.ALT_ARG,
        dest=Terms.MainParser.Generate.DEST,
        help=Terms.MainParser.Generate.HELP,
        default=Terms.MainParser.Generate.DEFAULT,
        action=Terms.ArgparseActions.STORE_TRUE
    )

    parser.add_argument(
        Terms.MainParser.IsProd.ARG,
        dest=Terms.MainParser.IsProd.DEST,
        help=Terms.MainParser.IsProd.HELP,
        default=Terms.MainParser.IsProd.DEFAULT,
        action=Terms.ArgparseActions.STORE_TRUE
    )

    return parser


def __generate(isProd: bool):
    print("generating...")


if (__name__ == "__main__"):
    main()

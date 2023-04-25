import subprocess
import sys
import typing
from argparse import SUPPRESS, ArgumentParser, Namespace
from dataclasses import dataclass, field
from os import path

import conf

# region constants
'''
    python required version based on pelican requirements
    info: https://docs.getpelican.com/en/latest/quickstart.html#installation
'''
REQUIRED_PYTHON_VERSION_MAJOR = 3
REQUIRED_PYTHON_VERSION_MINOR = 7
WORKSPACE_PATH = path.dirname(path.abspath(__file__))
# endregion


# region types
ParserHandler = typing.Callable[[Namespace], None]


@dataclass(init=False, frozen=True)
class Attributes:
    ParserHandler = "parserHandler"
    IsProd = "isProd"
    OutputDev = "output"
    OutputProd = "site"


@dataclass
class ParserOption:
    arg: str
    dest: str
    help: str
    action: str  # info: https://docs.python.org/3/library/argparse.html#action


@dataclass()
class Parser:
    name: str
    description: str
    handler: ParserHandler
    options: typing.List[ParserOption] = field(default_factory=list)
# endregion


# region functions
def main(args: typing.List[str]) -> None:
    if not __isPythonVersionvalid():
        exit(f"{path.basename(__file__)} requires python version {REQUIRED_PYTHON_VERSION_MAJOR}.{REQUIRED_PYTHON_VERSION_MINOR}+ ro tun.")

    parser = __buildArgumentParser()

    if not any(args):
        parser.print_help()
        exit()

    namespace = parser.parse_args(args)
    handler: ParserHandler = getattr(
        namespace,
        Attributes.ParserHandler
    )
    handler(namespace)


def __isPythonVersionvalid() -> bool:
    installed = (sys.version_info.major, sys.version_info.minor)
    required = (REQUIRED_PYTHON_VERSION_MAJOR, REQUIRED_PYTHON_VERSION_MINOR)

    return installed >= required


def __buildArgumentParser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Executes automated tasks of the project."
    )

    subparsers = parser.add_subparsers()

    for item in __getSubparsers():
        subparser = subparsers.add_parser(
            item.name,
            help=item.description,
            description=item.description
        )

        subparser.add_argument(
            "--parser-handler",
            dest=Attributes.ParserHandler,
            type=ParserHandler,
            default=item.handler,
            help=SUPPRESS
        )

        for option in item.options:
            subparser.add_argument(
                option.arg,
                dest=option.dest,
                help=option.help,
                action=option.action
            )

    return parser


def __getSubparsers() -> typing.List[Parser]:
    return [
        Parser(
            name="build",
            description="Builds the project and generates the site content",
            handler=__handleBuildParser,
            options=[
                ParserOption(
                    arg="--is-prod",
                    dest=Attributes.IsProd,
                    help="If included, the site content will be generated in the production directory",
                    action="store_true"
                )
            ]
        ),
        Parser(
            name="serve",
            description="Starts the development environment server",
            handler=__handleServeParser
        )
    ]


def __handleBuildParser(namespance: Namespace) -> None:
    isProd = getattr(namespance, Attributes.IsProd, False)
    outputName = Attributes.OutputProd if isProd else Attributes.OutputDev
    outputPath = path.join(WORKSPACE_PATH, outputName)
    __runCommand([], outputPath)


def __handleServeParser(_: Namespace) -> None:
    __runCommand(
        options=[
            "--listen",
            "--autoreload"
        ]
    )


def __runCommand(options: typing.List[str], outputPath: str = path.join(WORKSPACE_PATH, Attributes.OutputDev)):
    contentPath = path.join(WORKSPACE_PATH, conf.PATH)
    settingsPath = path.abspath(conf.__file__)
    command = f"{sys.executable} -m pelican {contentPath} --output {outputPath} --delete-output-directory --settings {settingsPath} {' '.join(options)}"
    subprocess.run(command.strip(), shell=True)
# endregion


if (__name__ == "__main__"):
    main(sys.argv[1:])

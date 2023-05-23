import subprocess
import sys
import typing
from argparse import SUPPRESS, ArgumentParser, Namespace
from dataclasses import dataclass, field
from datetime import datetime, timezone
from os import path

import conf_base
import conf_prod

# region constants

# python required version based on pelican requirements
# info: https://docs.getpelican.com/en/latest/quickstart.html#installation
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
    Title = "title"
    Status = "status"
    Statuses = ["draft", "published", "hidden"]


@dataclass
class ParserOption:
    arg: str
    dest: str
    help: str
    action: str  # info: https://docs.python.org/3/library/argparse.html#action
    required: bool = False
    choices: typing.List[typing.Any] = None


@dataclass()
class Parser:
    name: str
    description: str
    handler: ParserHandler
    options: typing.List[ParserOption] = field(default_factory=list)
# endregion


def main(args: typing.List[str]) -> None:
    if not __isPythonVersionvalid():
        exit(f"{path.basename(__file__)} requires python version {REQUIRED_PYTHON_VERSION_MAJOR}.{REQUIRED_PYTHON_VERSION_MINOR}+ ro tun.")

    parser = __buildArgumentParser()

    if not any(args):
        parser.print_help()
        exit()

    namespace = parser.parse_args(args)
    handler: ParserHandler = getattr(namespace, Attributes.ParserHandler)
    handler(namespace)


def __isPythonVersionvalid() -> bool:
    installed = (sys.version_info.major, sys.version_info.minor)
    required = (REQUIRED_PYTHON_VERSION_MAJOR, REQUIRED_PYTHON_VERSION_MINOR)

    return installed >= required


def __buildArgumentParser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Executes automated tasks of the project.")

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
            help=SUPPRESS,
        )

        for option in item.options:
            kargs = {
                "dest": option.dest,
                "help": option.help,
                "action": option.action
            }

            if (option.choices is not None and any(option.choices)):
                kargs["choices"] = option.choices

            subparser.add_argument(
                option.arg,
                **kargs
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
        ),
        Parser(
            name="generate",
            description="Generates a new time-stampped article file.",
            handler=__handleGenerateParser,
            options=[
                ParserOption(
                    arg="--title",
                    dest=Attributes.Title,
                    help="The new article title. It will also be used as fileaname (Spaces will be replaced with hyphens).",
                    action="store",
                    required=True
                ),
                ParserOption(
                    arg="--status",
                    dest=Attributes.Status,
                    help="The published status for the new article (defaults to \"draft\").",
                    action="store",
                    required=False,
                    choices=Attributes.Statuses
                )
            ]
        )
    ]


def __handleBuildParser(namespance: Namespace) -> None:
    isProd = getattr(namespance, Attributes.IsProd, False)
    options = ["--ignore-cache"] if isProd else []
    conf = conf_prod if isProd else conf_base
    __runPelicanCommand(options, conf)


def __handleServeParser(_: Namespace) -> None:
    __runPelicanCommand(options=["--listen", "--autoreload"])


def __handleGenerateParser(namespance: Namespace) -> None:
    title = str(
        getattr(namespance, Attributes.Title, "")
    ).strip()
    status = str(
        getattr(namespance, Attributes.Status, "draft")
    )

    utcTime = datetime.now(timezone.utc)
    date = utcTime.strftime('%Y-%m-%d')
    slug = title.replace(' ', '-')
    fileName = f"{date}_{slug}.md"
    filePath = path.join(WORKSPACE_PATH, conf_base.PATH, fileName)

    timeStamp = utcTime.strftime('%Y-%m-%d %H:%M')
    with open(filePath, mode="x") as file:
        lines = "\n".join([
            "---",
            f"title: {title}",
            f"date: {timeStamp}",
            f"modified: {timeStamp}",
            f"tags: none",
            f"slug: {slug}",
            f"author: {conf_base.SITENAME}",
            f"summary: {title}",
            f"status: {status}",
            "---"
        ]) + ("\n" * 2)
        file.write(lines)

    __runCommand(f"code {filePath} --reuse-window")


def __runPelicanCommand(options: typing.List[str], conf=conf_base):
    contentPath = path.join(WORKSPACE_PATH, conf.PATH)
    outputPath = path.join(WORKSPACE_PATH, conf.OUTPUT)
    settingsPath = path.abspath(conf.__file__)

    __runCommand(
        f"{sys.executable} -m pelican {contentPath} --output {outputPath} --delete-output-directory --settings {settingsPath} {' '.join(options)}"
    )


def __runCommand(command: str):
    subprocess.run(command.strip(), shell=True)


if __name__ == "__main__":
    main(sys.argv[1:])

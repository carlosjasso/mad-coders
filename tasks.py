import subprocess
import sys
import typing
from abc import ABC
from argparse import SUPPRESS, ArgumentParser, Namespace, _SubParsersAction
from dataclasses import dataclass, field
from datetime import datetime, timezone
from inspect import signature
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
class Terms:
    ParserHandler = "parserHandler"
    IsProd = "isProd"
    Title = "title"
    Status = "status"


@dataclass
class ParserArgument:
    flag: str
    name: str
    help: str
    action: str  # info: https://docs.python.org/3/library/argparse.html#action
    required: bool = False
    choices: typing.List[typing.Any] = field(default_factory=list)


@dataclass
class ParserBase(ABC):
    name: str
    description: str
    handler: ParserHandler = None
    arguments: typing.List[ParserArgument] = field(default_factory=list)


@dataclass
class SubParser(ParserBase):
    pass


@dataclass
class Parser(ParserBase):
    subparsers: typing.List[SubParser] = field(default_factory=list)


@dataclass
class Article():
    title: str
    date: str
    modified: str
    tags: str
    slug: str
    author: str
    summary: str
    status: str
    basename: str
    path: str
# endregion


def main(args: typing.List[str]) -> None:
    if not __isPythonVersionvalid():
        exit(f"{path.basename(__file__)} requires python version {REQUIRED_PYTHON_VERSION_MAJOR}.{REQUIRED_PYTHON_VERSION_MINOR}+ ro tun.")

    parser = __initArgumentParser()

    if not any(args):
        parser.print_help()
        exit()

    __handlerParser(parser, args)


# region argument parser init
def __initArgumentParser() -> ArgumentParser:
    rootParser = ArgumentParser(
        description="Executes automated tasks of the project."
    )

    rootContainer = rootParser.add_subparsers()

    for parserObject in __getParsers():
        parser = __attachSubParser(rootContainer, parserObject)

        if any(parserObject.subparsers):
            container = parser.add_subparsers()
            for subParserObject in parserObject.subparsers:
                __attachSubParser(container, subParserObject)

    return rootParser


def __getParsers() -> typing.List[Parser]:
    return [
        __initBuildParser(),
        __initServeParser(),
        __initArticleParser()
    ]


def __attachSubParser(container: _SubParsersAction, parserObject: Parser) -> ArgumentParser:
    parser: ArgumentParser = container.add_parser(
        parserObject.name,
        **__getParserArgsDict(parserObject)
    )

    __attachParcerArguments(
        parser,
        parserObject.handler,
        parserObject.arguments
    )

    return parser


def __attachParcerArguments(parser: ArgumentParser, handler: ParserHandler, arguments: typing.List[ParserArgument]) -> None:
    parser.add_argument(
        "--parser-handler",
        **__getParserHandlerArgsDict(handler or parser.print_help)
    )

    for argument in arguments:
        parser.add_argument(
            argument.flag,
            **__getParserArgumentArgsDict(argument)
        )


def __initBuildParser() -> Parser:
    return Parser(
        name="build",
        description="Builds the project and generates the site content",
        handler=__handleBuildParser,
        arguments=[
            ParserArgument(
                flag="--is-prod",
                name=Terms.IsProd,
                help="If included, the site content will be generated in the production directory",
                action="store_true"
            )
        ]
    )


def __initServeParser() -> Parser:
    return Parser(
        name="serve",
        description="Starts the development environment server",
        handler=__handleServeParser
    )


def __initArticleParser() -> Parser:
    return Parser(
        name="article",
        description="Utility tasks for article creation and manipulation.",
        subparsers=[
            SubParser(
                name="new",
                description="Create a new scaffolded article file.",
                handler=__handleNewArticleParser,
                arguments=[
                    ParserArgument(
                        flag="--title",
                        name=Terms.Title,
                        help="The new article title. It will also be used as fileaname (Spaces will be replaced with hyphens).",
                        action="store",
                        required=True
                    ),
                    ParserArgument(
                        flag="--status",
                        name=Terms.Status,
                        help="The published status for the new article (defaults to \"draft\").",
                        action="store",
                        choices=["draft", "published", "hidden"]
                    )
                ]
            )
        ]
    )
# endregion


# region argument parser handlers
def __handleBuildParser(namespace: Namespace) -> None:
    isProd = getattr(namespace, Terms.IsProd, False)
    options = ["--ignore-cache"] if isProd else []
    conf = conf_prod if isProd else conf_base
    __runPelicanCommand(options, conf)


def __handleServeParser(_: Namespace) -> None:
    __runPelicanCommand(options=["--listen", "--autoreload"])


def __handleNewArticleParser(namespace: Namespace) -> None:
    title = str(
        getattr(namespace, Terms.Title, "")
    ).strip()

    status = str(
        getattr(namespace, Terms.Status, "draft")
    )

    article = __initArticle(title, status)

    with open(article.path, mode="x") as file:
        frontmatter = __getFrontMatter(article)
        file.write(frontmatter)

    __runCommand(f"code {article.path} --reuse-window")
# endregion


# region helpers
def __isPythonVersionvalid() -> bool:
    installed = (sys.version_info.major, sys.version_info.minor)
    required = (REQUIRED_PYTHON_VERSION_MAJOR, REQUIRED_PYTHON_VERSION_MINOR)

    return installed >= required


def __getParserArgsDict(parser: ParserBase) -> typing.Dict[str, str]:
    return {
        "help": parser.description,
        "description": parser.description
    }


def __getParserHandlerArgsDict(handler: ParserHandler) -> typing.Dict[str, typing.Any]:
    return {
        "dest": Terms.ParserHandler,
        "type": ParserHandler,
        "default": handler,
        "help": SUPPRESS,
    }


def __getParserArgumentArgsDict(argument: ParserArgument) -> typing.Dict[str, typing.Any]:
    value = {
        "dest": argument.name,
        "help": argument.help,
        "action": argument.action,
        "required": argument.required
    }

    if any(argument.choices):
        value["choices"] = argument.choices

    return value


def __handlerParser(parser: ArgumentParser, args: typing.List[str]) -> None:
    namespace = parser.parse_args(args)
    handler: function = getattr(namespace, Terms.ParserHandler)
    if "argparse.Namespace" in str(signature(handler)):
        handler(namespace)
    else:
        handler()


def __initArticle(title: str, status: str) -> Article:
    utcTime = datetime.now(timezone.utc)
    timestamp = utcTime.isoformat(timespec="seconds")
    slug = title.replace(' ', '-')
    basename = f"{utcTime.strftime('%Y-%m-%d')}_{slug}.md"

    return Article(
        title=title,
        status=status,
        date=timestamp,
        modified=timestamp,
        tags=None,
        slug=slug,
        author=conf_base.SITENAME,
        summary=title,
        basename=basename,
        path=path.join(WORKSPACE_PATH, conf_base.PATH, basename)
    )


def __getFrontMatter(article: Article) -> str:
    return "\n".join([
        "---",
        f"title: {article.title}",
        f"date: {article.date}",
        f"modified: {article.modified}",
        f"tags: {article.tags or 'None'}",
        f"slug: {article.slug}",
        f"author: {article.author}",
        f"summary: {article.summary}",
        f"status: {article.status}",
        "---"
    ]) + ("\n" * 2)


def __runPelicanCommand(options: typing.List[str], conf=conf_base):
    contentPath = path.join(WORKSPACE_PATH, conf.PATH)
    outputPath = path.join(WORKSPACE_PATH, conf.OUTPUT)
    settingsPath = path.abspath(conf.__file__)

    __runCommand(
        f"{sys.executable} -m pelican {contentPath} --output {outputPath} --delete-output-directory --settings {settingsPath} {' '.join(options)}"
    )


def __runCommand(command: str):
    subprocess.run(command.strip(), shell=True)
# endregion


if __name__ == "__main__":
    main(sys.argv[1:])

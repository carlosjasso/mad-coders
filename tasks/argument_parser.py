import typing
from argparse import SUPPRESS, ArgumentParser, _SubParsersAction

from tasks import article_handler, build_handler, serve_handler
from tasks.types import (Parser, ParserArgument, ParserBase, ParserHandler,
                         PassiveParser, Terms)


def parseArgs(args: typing.List[str]) -> None:
    parser = __initArgumentParser()

    if not any(args):
        parser.print_help()
        exit()

    __handleParser(parser, args)


def __initArgumentParser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Executes automated tasks of the project."
    )

    __attachSubParsers(parser, __getParsers())

    return parser


def __getParsers() -> typing.List[ParserBase]:
    return [
        __initBuildParser(),
        __initServeParser(),
        __initArticleParser()
    ]


def __initBuildParser() -> Parser:
    return Parser(
        name="build",
        description="Builds the project and generates the site content",
        handler=build_handler.build,
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
        handler=serve_handler.serve
    )


def __initArticleParser() -> PassiveParser:
    return PassiveParser(
        name="article",
        description="Utility tasks for article creation and manipulation.",
        subparsers=[
            __initNewArticleParser(),
            __initArticleUtilsParser()
        ]
    )


def __initNewArticleParser() -> Parser:
    return Parser(
        name="new",
        description="Create a new scaffolded article file.",
        handler=article_handler.createArticle,
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


def __initArticleUtilsParser() -> Parser:
    return Parser(
        name="utils",
        description="Utilities for the article files.",
        handler=article_handler.processUtils,
        arguments=[
            ParserArgument(
                flag="--timestamp",
                name=Terms.Timestamp,
                help="Prints an ISO-8601 formatted timestamp with the current time in UTC.",
                action="store_true"
            )
        ]
    )


def __attachSubParsers(root: ArgumentParser, parsers: typing.List[ParserBase]) -> None:
    subparsers = root.add_subparsers()

    for parser in parsers:
        subparser = __attachSubParser(subparsers, parser)

        if isinstance(parser, PassiveParser):
            __attachSubParsers(subparser, parser.subparsers)


def __attachSubParser(subparser: _SubParsersAction, parserObject: ParserBase) -> ArgumentParser:
    parser: ArgumentParser = subparser.add_parser(
        parserObject.name,
        **__getParserArgsDict(parserObject)
    )

    handler = parserObject.handler \
        if isinstance(parserObject, Parser) \
        else __getPrintHelpHandler(parser)

    arguments = parserObject.arguments \
        if isinstance(parserObject, Parser) \
        else []

    __attachParcerArguments(
        parser,
        handler,
        arguments
    )

    return parser


def __getPrintHelpHandler(parser: ArgumentParser) -> ParserHandler:
    printHelp: ParserHandler = lambda _: parser.print_help()
    return printHelp


def __getParserArgsDict(parser: ParserBase) -> typing.Dict[str, str]:
    return {
        "help": parser.description,
        "description": parser.description
    }


def __attachParcerArguments(parser: ArgumentParser, handler: ParserHandler, arguments: typing.List[ParserArgument]) -> None:
    parser.add_argument(
        "--parser-handler",
        **__getParserHandlerArgsDict(handler)
    )

    for argument in arguments:
        parser.add_argument(
            argument.flag,
            **__getParserArgumentArgsDict(argument)
        )


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


def __handleParser(parser: ArgumentParser, args: typing.List[str]) -> None:
    namespace = parser.parse_args(args)
    handler: ParserHandler = getattr(namespace, Terms.ParserHandler)
    handler(namespace)

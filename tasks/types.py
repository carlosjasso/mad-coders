import typing
from abc import ABC as Abstract
from argparse import Namespace
from dataclasses import dataclass, field

ParserHandler = typing.Callable[[Namespace], None]


@dataclass(init=False, frozen=True)
class Terms:
    ParserHandler = "parserHandler"
    IsProd = "isProd"
    Timestamp = "isTimestamp"
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
class ParserBase(Abstract):
    name: str
    description: str


@dataclass
class Parser(ParserBase):
    handler: ParserHandler = None
    arguments: typing.List[ParserArgument] = field(default_factory=list)


@dataclass
class PassiveParser(ParserBase):
    subparsers: typing.List[Parser] = field(default_factory=list)


@dataclass
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


@dataclass
class BuildHandlerProps():
    isProd: bool = False


@dataclass
class ArticleUtilsProps():
    isTimestamp: bool = False


@dataclass
class CreateArticleProps():
    title: str = ""
    status: str = "draft"

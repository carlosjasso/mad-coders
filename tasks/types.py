import typing
from abc import ABC
from argparse import Namespace
from dataclasses import dataclass, field

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


@dataclass
class BuildHandlerProps():
    isProd: bool = False


@dataclass
class CreateArticleProps():
    title: str = ""
    status: str = "draft"

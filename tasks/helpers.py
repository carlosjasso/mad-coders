import typing
from argparse import Namespace
from os import environ, path

from pelican import Pelican
from pelican.settings import read_settings

import conf

T = typing.TypeVar("T")


def getSiteSettings(
    outputPath: str = conf.OUTPUT_DEV,
    minifyJS: bool = False,
    minifyCSS: bool = False
) -> typing.Dict[str, typing.Any]:
    environ["LIBSASS_STYLE"] = "compressed" if minifyCSS else "nested"

    settings = read_settings(path.abspath(conf.__file__))
    settings["OUTPUT_PATH"] = path.join(conf.WORKSPACE_PATH, outputPath)
    settings["JS_FILTER"] = "rjsmin" if minifyJS else None

    return settings


def buildSite(settings: typing.Dict[str, typing.Any]) -> None:
    pelican = Pelican(settings)
    pelican.run()


def getProps(namespace: Namespace, propsType: T) -> T:
    builder = type(typing.Type[propsType])

    for attribute in propsType.__annotations__:
        default = getattr(propsType, attribute)
        value = getattr(namespace, attribute, default) or default
        setattr(builder, attribute, value)

    return builder

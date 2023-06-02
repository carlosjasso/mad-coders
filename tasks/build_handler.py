import typing
from argparse import Namespace

import conf
from tasks import helpers
from tasks.types import BuildHandlerProps


def build(namespace: Namespace) -> None:
    props = helpers.getProps(namespace, BuildHandlerProps)

    outputPath = conf.OUTPUT_PROD if props.isProd else conf.OUTPUT_DEV
    settings = helpers.getSiteSettings(outputPath, props.isProd, props.isProd)
    helpers.buildSite(settings)

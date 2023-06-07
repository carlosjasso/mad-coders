from argparse import Namespace
from os import path

from livereload import Server

import conf
from tasks import helpers


def serve(_: Namespace) -> None:
    settings = helpers.getSiteSettings()
    helpers.buildSite(settings)

    server = __initServer()
    server.serve()


def __initServer() -> Server:
    server = Server()
    __setupServerWatcher(server)
    server.root = path.join(conf.WORKSPACE_PATH, conf.OUTPUT_DEV)

    return server


def __setupServerWatcher(server: Server) -> None:
    for watchedPath in [
        path.join(conf.WORKSPACE_PATH, conf.PATH),
        path.join(conf.WORKSPACE_PATH, conf.THEME),
        path.abspath(path.abspath(conf.__file__))
    ]:
        server.watch(watchedPath, __rebuildSite)


def __rebuildSite() -> None:
    settings = helpers.getSiteSettings()
    settings["CACHE_CONTENT"] = True
    settings["LOAD_CONTENT_CACHE"] = True

    helpers.buildSite(settings)

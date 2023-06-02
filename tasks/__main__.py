import sys
import typing

import conf
from tasks import argument_parser


def main(args: typing.List[str]) -> None:
    if not __isPythonVersionvalid():
        exit(f"{__package__} requires python version {conf.REQUIRED_PYTHON_VERSION_MAJOR}.{conf.REQUIRED_PYTHON_VERSION_MINOR}+ ro tun.")

    argument_parser.parseArgs(args)


def __isPythonVersionvalid() -> bool:
    installed = (sys.version_info.major, sys.version_info.minor)
    required = (conf.REQUIRED_PYTHON_VERSION_MAJOR,
                conf.REQUIRED_PYTHON_VERSION_MINOR)

    return installed >= required


if __name__ == "__main__":
    main(sys.argv[1:])

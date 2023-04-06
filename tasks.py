import sys
from argparse import ArgumentParser

REQUIRED_PYTHON_VERSION_MAJOR = 3
REQUIRED_PYTHON_VERSION_MINOR = 7


def main():
    __validate_python_version()
    parser = __build_parser()

    if (len(sys.argv) == 1):
        parser.print_help()
        exit()

    args = parser.parse_args()
    print(args)


def __validate_python_version() -> None:
    installed = (sys.version_info.major, sys.version_info.minor)
    required = (REQUIRED_PYTHON_VERSION_MAJOR, REQUIRED_PYTHON_VERSION_MINOR)
    if (installed < required):
        exit(f"{__file__} requires python version {REQUIRED_PYTHON_VERSION_MAJOR}.{REQUIRED_PYTHON_VERSION_MINOR}+ ro tun.")


def __build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Helps with automated tasks of the project."
    )

    # options
    parser.add_argument(
        "--is-prod",
        dest="IS_PROD",
        help="Include it to specify that command must be executed for production.",
        action="store_true",
        default=False
    )

    return parser


if (__name__ == "__main__"):
    main()

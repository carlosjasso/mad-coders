from sys import version_info as python_version, exit, argv
from argparse import ArgumentParser

required_version_major = 3
required_version_minor = 6

def main():
    __validate_runtime_version()
    
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(
        title="Options"
    )

    setup_parser = subparsers.add_parser("setup", help="Helps setup different aspects of the project")
    other_parser = subparsers.add_parser("other", help="Lorem ipsum dolot...")

    # setup_action = parser.add_argument("setup", help="Helps setup different aspects of the project")
    # setup_action = parser.add_argument("other", help="Lorem ipsum dolot...")
    
    # setup_group = parser.add_argument_group("setup arguments")
    # setup_options = setup_group.add_mutually_exclusive_group()
    # setup_options.add_argument(
    #     "--venv", 
    #     action="store_true",
    #     help="Checks for presense of the venv module (installs it, if needed) and generates a venv directory."
    # )

    if(len(argv) == 1):
        parser.print_help()
    else:
        print(parser.parse_args())
    
def __validate_runtime_version():
    runtime_version = (python_version.major, python_version.minor)
    required_version = (required_version_major, required_version_minor)
    if(runtime_version < required_version):
        exit(f"{__file__} requires python version {required_version_major}.{required_version_minor}+")


if (__name__ == "__main__"):
    main()

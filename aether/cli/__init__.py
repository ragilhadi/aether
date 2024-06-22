from argparse import ArgumentParser
from aether import __version__


def main():
    parser = ArgumentParser(description="Aether CLI")
    sub_parsers = parser.add_subparsers(dest="mode", help="Mode to run")
    parser.add_argument(
        "--version",
        action="version",
        version=f"aether version {__version__}",
    )

    args = parser.parse_args()
    if args.mode is None:
        parser.print_help()
        return

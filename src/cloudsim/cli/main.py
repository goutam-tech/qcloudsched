"""QCloudSched command-line interface."""

from __future__ import annotations

import argparse
import sys

from cloudsim import __version__


def create_parser() -> argparse.ArgumentParser:
    """Create the QCloudSched command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="QCloudSched",
        description=("QCloudSched - A Python-native cloud computing simulation framework."),
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="commands",
    )

    # ------------------------------------------------------------------
    # info
    # ------------------------------------------------------------------
    info_parser = subparsers.add_parser(
        "info",
        help="Display information about QCloudSched.",
    )
    info_parser.set_defaults(func=cmd_info)

    # ------------------------------------------------------------------
    # version
    # ------------------------------------------------------------------
    version_parser = subparsers.add_parser(
        "version",
        help="Display the QCloudSched version.",
    )
    version_parser.set_defaults(func=cmd_version)

    return parser


def cmd_info(_args: argparse.Namespace) -> int:
    """Display QCloudSched information."""
    print()
    print("QCloudSched")
    print("=" * 40)
    print("Python-native cloud computing simulation framework")
    print()
    print(f"Version : {__version__}")
    print("Purpose : Cloud infrastructure simulation")
    print("         Resource allocation")
    print("         Scheduling algorithms")
    print("         VM management")
    print("         Performance analysis")
    print()

    return 0


def cmd_version(_args: argparse.Namespace) -> int:
    """Display the installed QCloudSched version."""
    print(__version__)
    return 0


def main() -> int:
    """Run the QCloudSched command-line interface."""
    parser = create_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        return args.func(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())

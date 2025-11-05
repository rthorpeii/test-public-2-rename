#!/usr/bin/env python3
"""
CLI Application for test-public-2-rename
A simple command-line interface tool.
"""
import argparse
import sys

__version__ = "1.0.0"


def cmd_hello(args):
    """Handle the hello command."""
    name = args.name if args.name else "World"
    print(f"Hello, {name}!")
    return 0


def cmd_version(args):
    """Handle the version command."""
    print(f"CLI version {__version__}")
    return 0


def cmd_info(args):
    """Handle the info command."""
    print("CLI Application for test-public-2-rename")
    print(f"Version: {__version__}")
    print("A simple command-line interface tool.")
    return 0


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        prog="test-cli",
        description="A simple CLI application",
        epilog="For more information, visit the repository."
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    
    subparsers = parser.add_subparsers(
        title="commands",
        description="Available commands",
        dest="command",
        help="Command to execute"
    )
    
    # Hello command
    hello_parser = subparsers.add_parser(
        "hello",
        help="Print a greeting message"
    )
    hello_parser.add_argument(
        "name",
        nargs="?",
        help="Name to greet (default: World)"
    )
    hello_parser.set_defaults(func=cmd_hello)
    
    # Version command
    version_parser = subparsers.add_parser(
        "version",
        help="Show version information"
    )
    version_parser.set_defaults(func=cmd_version)
    
    # Info command
    info_parser = subparsers.add_parser(
        "info",
        help="Show information about this CLI"
    )
    info_parser.set_defaults(func=cmd_info)
    
    # Parse arguments
    args = parser.parse_args()
    
    # If no command is provided, show help
    if not hasattr(args, "func"):
        parser.print_help()
        return 0
    
    # Execute the command
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

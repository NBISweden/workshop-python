#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pyhead.py - A cross-platform Python script that mimics the basic functionality
of the Unix 'head' command.

Usage:
    python pyhead.py -n 2 filename.gtf
    python pyhead.py file1.fasta file2.gtf
"""

import argparse
import sys

def print_head(filepath: str, num_lines: int) -> bool:
    """
    Reads and prints the first N lines of a file.
    Returns True if successful, False if an error occurred.
    """
    if num_lines <= 0:
        return True

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as file:
            for index, line in enumerate(file):
                if index >= num_lines:
                    break
                print(line, end="")
        return True
    except FileNotFoundError:
        print(f"Error: Could not find file '{filepath}'", file=sys.stderr)
        return False
    except PermissionError:
        print(f"Error: Permission denied reading '{filepath}'", file=sys.stderr)
        return False
    except Exception as error:
        print(f"Error reading '{filepath}': {error}", file=sys.stderr)
        return False

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print the first N lines of a file."
    )
    parser.add_argument(
        "files",
        nargs="+",
        metavar="FILE",
        help="One or more file paths to read",
    )
    parser.add_argument(
        "-n",
        "--lines",
        type=int,
        default=10,
        metavar="LINES",
        help="Number of lines to print (default: 10)",
    )

    args = parser.parse_args()

    show_header = len(args.files) > 1
    has_errors = False
    broken_pipe = False

    for index, filepath in enumerate(args.files):
        if show_header:
            if index > 0:
                try:
                    print()  # Add space between multiple files
                except BrokenPipeError:
                    broken_pipe = True
                    break
            try:
                print(f"==> {filepath} <==")
            except BrokenPipeError:
                broken_pipe = True
                break

        try:
            success = print_head(filepath, args.lines)
            if not success:
                has_errors = True
        except BrokenPipeError:
            broken_pipe = True
            break

    # Single exit point in main()
    if broken_pipe:
        sys.exit(0)

    sys.exit(1 if has_errors else 0)

if __name__ == "__main__":
    main()

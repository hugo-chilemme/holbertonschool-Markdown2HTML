#!/usr/bin/python3
"""
Script to convert markdown to HTML
"""
import sys


def main():
    """
    Main function for markdown2html.py
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()

    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]),
              file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()

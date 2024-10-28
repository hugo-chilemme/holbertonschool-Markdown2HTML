#!/usr/bin/python3
"""
Script to convert markdown to HTML
"""
import sys


def analyze_line(line):
    """
    Analyze a line of Markdown and convert it to HTML
    """
    countHashtag = 0
    line = line.strip()
    for c in line:
        if ["#", " ", "\t"] == list(c):
            line = line[1:]
            if c == '#':
                countHashtag += 1
        else:
            break

    if countHashtag == 0:
        return line

    return "<h{}>{}</h{}>".format(countHashtag, line, countHashtag)


def main():
    """
    Main function for markdown2html.py
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    try:

        result = ""
        with open(sys.argv[1], 'r') as f:

            lines = f.readlines()
            for line in lines:
                result += analyze_line(line) + "\n"

            with open(sys.argv[2], 'w') as f:
                f.write(result)

    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]),
              file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Script to convert markdown to HTML
"""
import sys


def analyze_header(line):
    """
    Analyze a header line of Markdown and convert it to HTML
    """
    countHashtag = line.split(" ")[0].count("#")

    return "<h{}>{}</h{}>".format(countHashtag, line, countHashtag)


def analyze_unordered(line, options):
    """
    Analyze an unordered list line of Markdown and convert it to HTML
    """
    if not options.get("Unordered"):
        options["Unordered"] = True
        return "<ul>\n\t<li>{}</li>".format(line[2:])
    elif not line or line[0] != '-':
        options["Unordered"] = False
        return "</ul>\n{}".format(analyze_line(line, options))

    return "\t<li>{}</li>".format(line[2:])


def analyze_line(line, options):
    """
    Analyze a line of Markdown and convert it to HTML
    """

    if options.get("Unordered"):
        return analyze_unordered(line, options)

    if not line or line == "":
        return ""

    if line[0] == "#":
        return analyze_header(line)

    if line[0] == '-':
        return analyze_unordered(line, options)

    return line


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

            options = {
                "Unordered": False,
            }

            for line in lines:

                line = line.strip()

                result += analyze_line(line, options) + "\n"

            analyze_line("", options)

            with open(sys.argv[2], 'w') as f:
                f.write(result)

    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]),
              file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()

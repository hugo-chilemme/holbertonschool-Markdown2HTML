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

    line = line.replace("#", "", countHashtag).strip()

    return "<h{}>{}</h{}>\n".format(countHashtag, line, countHashtag)


def analyze_unordered(lines, mode="-"):
    """
    Analyze an unordered list line of Markdown and convert it to HTML
    """

    if not lines:
        return "", 0

    base = "ul"
    if mode == "*":
        base = "ol"

    results = "<{}>\n".format(base)
    cut = 0
    for line in lines:
        if ["-", "*"].count(line[0]) == 1:
            cut += 1
            results += "\t<li>" + line[1:].strip() + "</li>\n"
            continue
        break

    if cut == 0:
        return "", 0

    results += "</{}>\n".format(base)

    return results, cut


def analyze_line(line):
    """
    Analyze a line of Markdown and convert it to HTML
    """

    if not line or line == "":
        return ""

    if line[0] == "#":
        return analyze_header(line)

    return line + "\n"


def main():
    """
    Main function for markdown2html.py
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    try:

        lines = ""
        with open(sys.argv[1], 'r') as f:

            lines = f.readlines()

        result = ""
        for line in lines:

            line = line.strip()

            if line:
                if ["-", "*"].count(line[0]) == 1:
                    res, cut = analyze_unordered(lines, line[0])
                    result += res

                    lines = lines[cut:]
                    continue

            lines = lines[1:]
            result += analyze_line(line)

        with open(sys.argv[2], 'w') as f:
            f.write(result)

    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]),
              file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()

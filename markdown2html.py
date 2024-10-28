#!/usr/bin/python3
"""
Script to convert markdown to HTML
"""
import sys
import datetime


def analyze_header(line):
    """
    Analyze a header line of Markdown and convert it to HTML
    """
    countHashtag = line.split(" ")[0].count("#")

    line = line.replace("#", "", countHashtag).strip()

    return "<h{}>{}</h{}>\n".format(countHashtag, line, countHashtag)


def analyse_paragraph(lines):
    """
    Analyze a paragraph of Markdown and convert it to HTML
    """
    results = []
    cut = 0
    for line in lines:
        if len(line.strip()) == 0:
            break
        results.append("\t" + line.strip())

        cut += 1

    if results == []:
        return "", 0

    return "<p>\n" + "\n\t\t<br />\n".join(results) + "\n</p>\n", cut


def analyze_unordered(lines, mode="-"):
    """
    Analyze an unordered list line of Markdown and convert it to HTML
    """
    if not lines:
        return "", 0

    base = mode == "-" and "ul" or "ol"

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

        result = "<!-- Generated at {} -->\n".format(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        for line in lines:

            line = line.strip()

            if not line:
                line = " "

            if ["-", "*"].count(line[0]) == 1:
                res, cut = analyze_unordered(lines, line[0])
                result += res

                lines = lines[cut:]
                continue

            if line[0] == "#":
                result += analyze_header(line)
                lines = lines[1:]
                continue

            if line == " ":
                lines = lines[1:]
                continue

            res, cut = analyse_paragraph(lines)

            result += res
            lines = lines[cut:]

        with open(sys.argv[2], 'w') as f:
            f.write(result)

    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]),
              file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()

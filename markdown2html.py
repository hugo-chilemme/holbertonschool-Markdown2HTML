#!/bin/python3
import sys

if (len(sys.argv) != 3):
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)
    
md_file = sys.argv[1]
html_file = sys.argv[2]


try:
    with open(md_file, 'r') as f:
        md_content = f.read()
except FileNotFoundError:
    print("Missing <filename>")
    exit(1)

exit(0)
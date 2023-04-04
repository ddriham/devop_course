#! /usr/bin python3

# this script ment to teach how to create args on linux using python
# The script reads a file and returns its contents in reversed

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', help ='the file to read' )
parser.add_argument('--limit', '-l',  type=int, help ='the number of lines to read' )
parser.add_argument('--version', '-v',  action='version', version='%(prog)s 1.0' )
args = parser.parse_args()


with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip()[::-1])

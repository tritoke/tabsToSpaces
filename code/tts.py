#!/usr/bin/env python3
from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument("file", help="the file in which to replace the tabs")
parser.add_argument("-s", "--spaces", type=int, help="the number of spaces to replace each tab with - defaults to 4", default=4)
args = parser.parse_args()

try:
    data = open(args.file, "rb").read()
    output = []
    for i in data:
        if i == ord("\t"):
            output+=[ord(" ")]*args.spaces
        else:
            output.append(i)
    open(args.file, "wb").write(bytes(output))
    # remove trailing spaces
    lines = open(args.file, "r").readlines()
    out = []
    for line in lines:
        for i, char in enumerate(line):
            if set(line[i:]) in [set([" ", "\n"]), set(["\n"])]:
                out.append(line[:i])
                break
    open(args.file, "w").write("\n".join(out))
except FileNotFoundError:
    print("file not found, try providing a full path")


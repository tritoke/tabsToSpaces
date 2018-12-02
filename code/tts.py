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
except FileNotFoundError:
    print("file not found, try providing a full path")


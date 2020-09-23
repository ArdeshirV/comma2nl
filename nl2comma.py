#!/usr/bin/env python3
# nl2comma - Convert Comma(s) in Text Files to New Lines, Version 1.0
# Copyright 2020 ArdeshirV@protonmail.com, Licensed under GPLv3+
from sys import argv, exit


def main(args):
    file_input = open(args[1], "r")
    contents = file_input.read()
    file_input.close()

    index = 0
    contents_len = len(contents)

    for i in range(0, contents_len):
        c = contents[index]
        if(c == ','):
            index += 1
            if contents_len <= index: break
            c = contents[index]
            print()
            if(contents[index] == ' '):
                index += 1
                if contents_len <= index: break
                c = contents[index]
        print(c, sep='', end='')
        index += 1
        if contents_len <= index: break


if __name__ == "__main__":
    exit(main(argv))


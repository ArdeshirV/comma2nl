#!/usr/bin/env python3
# comma2nl - Convert Comma(s) in Text Files to New Lines, Version 1.0
# Copyright 2020 ArdeshirV@protonmail.com, Licensed under GPLv3+
from sys import argv, exit


def main(args):
    if len(args) < 2:
        print("\033[0;31mError: \033[1;31mYou sould"
              " specify a file name to process!\033[0m")
        return -1
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

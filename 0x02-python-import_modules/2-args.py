#!/usr/bin/python3

import sys


def main():
    args = sys.argv[1:]
    arglstlen = len(args)

    if arglstlen == 1:
        print(f"1 argument:")
    else:
        print(f"{arglstlen} arguments:")

    for i in range(arglstlen):
        print(f"{i + 1}: {args[i]}")


if __name__ == '__main__':
    main()

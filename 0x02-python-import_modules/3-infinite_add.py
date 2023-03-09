#!/usr/bin/python
import sys

def main():
    args = sys.argv[1:]
    arg_len = len(args)

    if arg_len == 1:
        print("1 argument")
    else:
        print(f"{arg_len} arguments")

    arg_sum = sum(int(arg) for arg in args)
    print(f"{arg_sum}")

if __name__ == '__main__':
    main()
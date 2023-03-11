#!/usr/bin/python3

def print_list_integer(my_list = []):
    length = len(my_list)

    for i in length:
        print("{i}", str.format(i))
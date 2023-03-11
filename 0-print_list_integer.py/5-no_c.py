#!/usr/bin/python3

def no_c(string):
    length = len(string)

    for i in range(length):
        if i == 'c' or i == 'C':
            continue
        else:
            print(f"{i}")

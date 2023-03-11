#!/usr/bin/python3

def no_c(string):
    length = len(string)
    new_string = ""

    for i in range(length):
        if string[i] == 'c' or string[i] == 'C':
            continue
        else:
            new_string += string[i]

    return new_string

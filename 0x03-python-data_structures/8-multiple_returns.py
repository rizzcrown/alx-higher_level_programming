#!/usr/bin/python3

def multiple_returns(sentence):
    string_length = len(sentence)
    first_char = sentence[0]

    if string_length == 0:
        return None
    else:
        return string_length, first_char

#!/usr/bin/python3
def islower(c):
    for i in c:
        if not 'a' <= i <= 'z':
            return False
        else:
            return True

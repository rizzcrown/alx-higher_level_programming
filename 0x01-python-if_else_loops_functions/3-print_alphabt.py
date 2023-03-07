#!/usr/bin/python3

for i in range(ord('A'), ord('Z') + 1):
    lower_letters = chr(i).lower()
    if lower_letters in ['q','e']:
        continue
    print(f"{lower_letters}", end="")


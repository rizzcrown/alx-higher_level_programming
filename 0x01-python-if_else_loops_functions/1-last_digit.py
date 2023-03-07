#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)

if number % 10 > 5:
    print(f"Last digit of {number} is {number % 10} and is greater than 5\n")
elif number % 10 == 0:
    print(f"Last digit of {number} is {number % 10} and is 0\n")
elif number % 10 > 0 and number % 10 < 6:
    print(f"Last digit of {number} is {number % 10} and is greater than 0 but less than 6\n")


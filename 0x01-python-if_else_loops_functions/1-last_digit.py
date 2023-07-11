#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = (number) % 10
if digit > 5:
    print("last digit is greater than 5")
elif digit == 0:
    print("last digit is equal to 0")
else:
    print("and is less than 6 and not 0")

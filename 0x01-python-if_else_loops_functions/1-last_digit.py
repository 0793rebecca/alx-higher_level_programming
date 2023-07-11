#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = (number) % 10
if digit > 5:
    print("last digit of {} is {} and is greater than 5".format(number, digit))
elif digit == 0:
    print("last digit of {} is {} and is equal to 0".format(number, digit))
else:
    print("and is less than 6 and not 0")

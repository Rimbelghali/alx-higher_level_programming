#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_unsigned = abs(number) % 10
if last_digit_unsigned > 5:
    print(f'Last digit of {number} is {last_digit_unsigned} and is greater than 5')
elif last_digit_unsigned == 0:
    print(f'Last digit of {number} is {last_digit_unsigned} and is 0')
else:
    print(f'Last digit of {number} is {last_digit_unsigned} and is less than 6 and not 0')

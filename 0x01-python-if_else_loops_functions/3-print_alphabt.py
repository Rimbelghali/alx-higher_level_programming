#!/usr/bin/python3
for letter_code in range(ord('a'), ord('z') + 1):
    letter = chr(letter_code)
    if letter != 'q' and letter != 'e':
        print('{0}'.format(letter), end='')

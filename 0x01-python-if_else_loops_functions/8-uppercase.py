#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        letter_rep = ord(alphabet)
        if letter_rep >= 97 and letter_rep <= 122:
            letter_rep = letter_rep - 32
        letter = chr(letter_rep)
        print('{}'.format(letter), end='')
    print('')

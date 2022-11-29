#!/usr/bin/python3
for number in range(0, 99):
    if number % 10 > number / 10:
        if number != 89:
            print("{:02}".format(number), end=', ')
        else:
            print("{:02}".format(number))

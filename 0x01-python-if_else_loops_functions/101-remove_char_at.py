#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    for a in range(len(str)):
        if a != n:
            new = new + str[a]
    return (new)

#!/usr/bin/python3
def remove_char_at(str, n):
    for value in range(0, len(str)):
        if n >= 0:
            return str[:n] + str[n + 1:]
        else:
            return str


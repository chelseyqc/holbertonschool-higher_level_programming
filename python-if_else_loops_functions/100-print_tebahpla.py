#!/usr/bin/python3
for c in range(122, 98, -1):
    if c % 2 == 1:
        c = c - 32
    print("{:c}".format(c), end="")

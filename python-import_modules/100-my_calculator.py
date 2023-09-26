#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
a = int(sys.argv[1])
b = int(sys.argv[3])
operator = sys.argv[2]
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end=" ")
        exit(1)
    elif operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))

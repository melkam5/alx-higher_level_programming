#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    size = len(sys.argv)
    if (size != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if (operator == "+"):
        print(a, "+", b, "=", add(a, b))
        sys.exit(0)
    elif (operator == "-"):
        print(a, "-", b, "=", sub(a, b))
        sys.exit(0)
    elif (operator == "*"):
        print(a, "*", b, "=", mul(a, b))
        sys.exit(0)
    elif (operator == "/"):
        print(a, "/", b, "=", div(a, b))
        sys.exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

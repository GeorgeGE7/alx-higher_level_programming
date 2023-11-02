#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def summingA(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    tshg = argv[2]
    b = int(argv[3])
    if tshg == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, tshg, b, add(a, b)))
    elif tshg == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, tshg, b, sub(a, b)))
    elif tshg == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, tshg, b, mul(a, b)))
    elif tshg == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, tshg, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    summingA(sys.argv)

#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    from sys import argv

    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
            exit(0)
        elif argv[2] == "-":
            print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
            exit(0)
        elif argv[2] == "*":
            print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
            exit(0)
        elif argv[2] == "/":
            print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
            exit(0)
        elif argv[2] != "+" or argv[2] != "-" or argv[2] != "*" or argv[2] != "/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

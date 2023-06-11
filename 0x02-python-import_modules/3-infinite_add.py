#!/usr/bin/python3
def arg_addition(av):
    add = 0
    for i in range(len(av) - 1):
        add += int(av[i + 1])
    print(f"{add}")


if __name__ == "__main__":
    import sys
    arg_addition(sys.argv)

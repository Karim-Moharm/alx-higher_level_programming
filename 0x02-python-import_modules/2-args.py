#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
        print(f"{argc}: {sys.argv[argc]}")
    else:
        print(f"{argc} arguments:")
        for i in range(argc):
            print(f"{i + 1}: {sys.argv[i + 1]}")

#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    # ord used to get the ascii value of char
    if i == ord('q') or i == ord('e'):
        continue
    print("{:c}".format(i), end="")

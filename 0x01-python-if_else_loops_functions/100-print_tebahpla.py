#!/usr/bin/python3
for i in range(ord('z'), ord('a'), -1):
    if i % 2:       #if ascii for char is odd, convert it to upper
        i = chr(i - 32)
    else:
        i = chr(i)
    print("{}".format(i), end="")

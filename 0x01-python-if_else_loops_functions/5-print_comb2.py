#!/usr/bin/python3
for i in range(100):
    print("0{:d}".format(i) if i < 10 else "{:d}".format(i), end=", ")
print()

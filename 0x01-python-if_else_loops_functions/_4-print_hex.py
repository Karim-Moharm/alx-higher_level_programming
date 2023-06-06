#!/usr/bin/python3
for i in range (98):
    print(f"{i} = 0x{i}" if i < 9 else f"{i} = 0x{str ((int(i) / 16) % 16) + str (int(i) % 16)}")

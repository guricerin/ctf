#!/usr/bin/env python3.8

import sys

enc = open(sys.argv[1]).read().split()
ans = ""
for e in enc:
    e = int(e) % 37
    if 0 <= e and e <= 25:
        ans += chr(e + 0x41)
    elif e <= 35:
        ans += chr(e - 26 + 0x30)
    else:
        ans += "_"
print("picoCTF{" + ans + "}")

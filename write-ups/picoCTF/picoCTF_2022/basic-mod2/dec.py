#!/usr/bin/env python3.8

import sys
from Crypto.Util.number import inverse

enc = open(sys.argv[1]).read().split()
ans = ""
for e in enc:
    e = inverse(int(e), 41)
    if 1 <= e and e <= 26:
        ans += chr(e - 1 + 0x41)
    elif e <= 36:
        ans += chr(e - 27 + 0x30)
    else:
        ans += "_"
print("picoCTF{" + ans + "}")

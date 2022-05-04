#!/usr/bin/env python3

import sys

filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    code = map(int, lines)
    s = ''.join(map(chr, code))
    print(s)

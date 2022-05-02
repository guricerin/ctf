#!/usr/bin/env python3.8

before = [0x7a, 0x69, 0x78, 0x6e, 0x62, 0x6f, 0x7c, 0x6b, 0x77, 0x78, 0x74, 0x38, 0x38, 0x64]
after = map((lambda b: b ^ 0x19), before)
after = map(chr, after)
after = ''.join(after)

before = map(chr, before)
before = ''.join(before)

print("before: {}".format(before))
print("after: {}".format(after))

#!/usr/bin/env python3.8

p = [70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196, 1520, 1480, 1449]
t = [0] * len(p)
for i in range(len(p)):
    t[i] = p[i] // (i+1)

print(t)
print(''.join(map(chr, t)))

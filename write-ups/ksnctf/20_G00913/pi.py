#!/usr/bin/env python3.8

import sympy

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
lim = len(pi) - 2
for i in range(2, lim - 10):
    n = int(pi[i:i + 10])
    if sympy.isprime(n):
        print(f"found!: FLAG_Q20_{n}")
        break

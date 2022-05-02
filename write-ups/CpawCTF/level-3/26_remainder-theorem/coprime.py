#!/usr/bin/env python3.8

import math

a, b = map(int, input().split())
# 互いに素？
print(math.gcd(a, b) == 1)

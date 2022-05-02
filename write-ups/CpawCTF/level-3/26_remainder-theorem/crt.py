#!/usr/bin/env python3.8
# 『詳解セキュリティコンテスト』p.296より引用

from functools import reduce

# 中国剰余定理
def crt(a, m):
    assert len(a) == len(m)
    # 各mod（m[0], m[1], ...）の総積
    # 各modは互いに素なので、結果的にはlcm(m[0], m[1], ...)と等しい
    MM = reduce(lambda a, b: a * b, m)
    x = 0
    for i in range(len(a)):
        Mi = MM // m[i]
        # m[i]を法としたときのMiの逆元 -> Mi * ti = 1 (mod m[i]) を満たすti
        ti = pow(Mi, -1, m[i])
        x += (Mi * ti * a[i]) % MM
    return x % MM

N = int(input())
A = []
M = []
for i in range(N):
    a, m = map(int, input().split())
    A.append(a), M.append(m)

x = crt(A, M)
print("cpaw{%d}" % x)

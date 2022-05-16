#!/usr/bin/env python3.8

code = [20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]
plain = [chr(0x40 + c) for c in code]
plain = ''.join(plain)
print("picoCTF{" + plain + "}")

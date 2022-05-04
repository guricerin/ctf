#!/usr/bin/env python3.8

import hashlib

username = b"FREEMAN"
h = hashlib.sha256(username).hexdigest()
print(h)
key = f"{h[4]}{h[5]}{h[3]}{h[6]}{h[2]}{h[7]}{h[1]}{h[8]}"
print(key)
print("picoCTF{1n_7h3_|<3y_of_" + key + "}")


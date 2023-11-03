#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

with urlopen("https://alx-intranet.hbtn.io/status") as response:
    read_url = response.read()
    output = read_url.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(read_url)))
    print("\t- content: {}".format(read_url))
    print("\t- utf8 content: {}".format(output))

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

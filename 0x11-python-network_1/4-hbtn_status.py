#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":
    url_argument = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url_argument)

    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))

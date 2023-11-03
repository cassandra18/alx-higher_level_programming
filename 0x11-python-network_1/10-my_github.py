#!/usr/bin/python3
"""
Takes Github credentials an uses the GITHUB API to display your ID.
"""

import sys
import requests

if __name__ == "__main__":

    auth = (sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))

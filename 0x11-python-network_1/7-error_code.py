#!/usr/bin/python3
"""
Send a request to URL and display the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url_argument = sys.argv[1]
    res = requests.get(url_argument)
    status_code = res.status_code
    if status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        print(res.text)

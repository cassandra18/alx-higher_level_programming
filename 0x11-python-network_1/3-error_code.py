#!/usr/bin/python3
"""
Send request to a body and display the response of the body.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url_argument = sys.argv[1]
    try:
        with urllib.request.urlopen(url_argument) as response:
            res = response.read().decode('utf-8')
            print(res)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

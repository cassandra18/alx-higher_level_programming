#!/usr/bin/python3
"""
Sen request to URL, display value of variable X-Request-Id.
"""
import sys
import requests

if __name__ == "__main__":
    url_argument = sys.argv[1]

    res = requests.get(url_argument)

    x_request_id = res.headers.get('X-Request-Id')
    print(x_request_id)

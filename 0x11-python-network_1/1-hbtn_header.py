#!/usr/bin/python3
"""Sen a request to URL and displays the value of X-Request-Id."""
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

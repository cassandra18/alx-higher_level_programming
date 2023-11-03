#!/usr/bin/python3
"""
Python script that takes in a URL and an email address.
Sends a POST request to the passed URL with the email as a parameter.
Finally displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":

    url_argument = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    res = requests.post(url_argument, data=payload)

    print("Your email is: {}".format(res.text.strip()))

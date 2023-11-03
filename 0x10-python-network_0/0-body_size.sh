#!/bin/bash
# A script that takes in a URL, sends a request to the URL, and displays the size of the body response.
curl -s "$1" | wc -c

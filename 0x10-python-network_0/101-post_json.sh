#!/bin/bash
# Sends a JSON POST request and displays body of response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

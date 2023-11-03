#!/bin/bash
# Send a GET request to URL, display response body.
curl -sX GET $1 -H "X-School-User-Id: 98" -L

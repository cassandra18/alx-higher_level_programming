#!/bin/bash
# Sends a request to URL, server responds with You got me
curl 0.0.0.0:5000/catch_me -X PUT -sL -d"user_id=98" -H"Origin: HolbertonSchool"

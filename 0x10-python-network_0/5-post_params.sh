#!/bin/bash
# Sen a POST request and display body of response
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L

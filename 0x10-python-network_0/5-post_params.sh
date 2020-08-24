#!/bin/bash
# takes a URL, sends a POST request to the URL, and displays the response
curl -s POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"

#!/usr/bin/python3
#  sends a request to URL and displays value of X-Request-Id
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))

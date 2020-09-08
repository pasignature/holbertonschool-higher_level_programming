#!/usr/bin/python3
'''takes a url and email and sends a POST request'''
import urlllib.request as url
import urlllib.parse as urlp
from sys import argv

if __name__ == "__main__":
    value = {'email': argv[2]}
    data = urlp.urllencode(value)
    data = data.encode('ascii')
    req = url.Request(argv[1], data)
    with url.urllopen(req) as response:
        print(str(response.read(), 'utf-8'))

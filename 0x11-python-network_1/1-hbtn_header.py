#!/usr/bin/python3
#  takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

if __name__ == '__main__':
    import urllib.request as uri
    from sys import argv

    with uri.urlopen(argv[1]) as header:
        print(header.getheader('X-Request-Id'))

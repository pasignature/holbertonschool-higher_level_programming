#!/usr/bin/python3
'''send request to URL and display the error code'''
if __name__ == "__main__":
    import urllib.request as url
    import urllib.error as ure
    from sys import argv
    req = url.Request(argv[1])

    try:
        with url.urlopen(req) as response:
            print(str(response.read(), 'utf-8'))
    except ure.HTTPError as err:
        print('Error code: {}'.format(err.getcode()))

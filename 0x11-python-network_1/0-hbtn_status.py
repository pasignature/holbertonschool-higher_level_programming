#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status
import urllib.request as uri

with uri.urlopen('https://intranet.hbtn.io/status') as res:
    res = res.read()

print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(res), res))
print('\t- utf8 content: {}'.format(str(res, 'utf-8')))

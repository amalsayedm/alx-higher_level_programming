#!/usr/bin/python3
"""Fetch url response"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    content = response.read()
print('Body response:')
print('\t- type: {}'.format(type(content)))
print('\t- content: {}'.format(content))
print('\t- utf8 content: {}'.format(str(content)[2:-1]))

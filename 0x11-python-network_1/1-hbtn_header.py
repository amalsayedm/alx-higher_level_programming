#!/usr/bin/python3
"""Fetches url response header"""
import urllib.request
import sys


request = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))

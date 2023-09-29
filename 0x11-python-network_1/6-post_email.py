#!/usr/bin/python3
"""Sends a POST request to a given URL with the  email"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}

    r = requests.post(url, data=data)
    print(r.text)

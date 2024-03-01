#!/usr/bin/python3
"""A script that: print the header X-Request-Id
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        response = dict(res.headers).get("X-Request-Id")
        print(response)

#!/usr/bin/python3
"""Print header value
"""
import sys
import requests


if __name__ == "__main__":
    alx_url = sys.argv[1]

    req = requests.get(alx_url)
    header_value = req.headers.get("X-Request-Id")
    print(header_value)

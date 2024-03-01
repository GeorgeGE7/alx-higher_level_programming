#!/usr/bin/python3
"""A script that send req and display body
"""
import sys
import requests


if __name__ == "__main__":
    alx_url = sys.argv[1]

    req = requests.get(alx_url)
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)

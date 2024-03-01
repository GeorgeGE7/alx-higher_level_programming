#!/usr/bin/python3
"""Fetch an URL from alx"""
import requests


if __name__ == "__main__":
    alx_url = "https://intranet.hbtn.io/status"
    request = requests.get(alx_url)
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))

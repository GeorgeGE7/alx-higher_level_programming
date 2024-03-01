#!/usr/bin/python3
"""A script that: get an email and url
"""
import sys
import requests

if __name__ == "__main__":
    t_email = {'email': sys.argv[2]}
    try:
        response = requests.post(sys.argv[1], data=t_email)
        response.raise_for_status()
        print(f"Your email is: {t_email}")
    except requests.exceptions.RequestException as errr:
        print("Error:", errr)

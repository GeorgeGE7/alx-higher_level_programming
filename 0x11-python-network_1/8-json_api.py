#!/usr/bin/python3
"""Using JSON API
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    t_latter = {"q": letter}
    t_url = "http://0.0.0.0:5000/search_user"

    req = requests.post(t_url, data=t_latter)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get("id")}] {response.get("name")}")
    except ValueError:
        print("Not a valid JSON")

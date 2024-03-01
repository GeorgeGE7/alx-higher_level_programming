#!/usr/bin/python3
"""list commits
"""
import sys
import requests


if __name__ == "__main__":
    # Repo url
    r_url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    req = requests.get(r_url)

    # repo commits
    r_c = req.json()
    try:
        for i in range(10):
            r_c_c = r_c[i].get("sha")
            r_c_A = r_c[i].get("commit").get("author").get("name")
            print(f"{r_c_c}: {r_c_A}")
    except Exception:
        pass

#!/usr/bin/python3
"""Error"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code == 200:
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")

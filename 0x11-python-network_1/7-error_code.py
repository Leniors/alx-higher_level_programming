#!/usr/bin/python3
"""Error"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    try:
        print(req.text)
    except:
        print(f"Error code: {req.status_code}")

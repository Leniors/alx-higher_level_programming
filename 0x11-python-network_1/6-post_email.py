#!/usr/bin/python3
"""post"""
import sys
import requests

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=data)
    print(response.text)

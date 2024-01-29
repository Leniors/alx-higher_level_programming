#!/usr/bin/python3
"""get"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- type: {response.reason}")

#!/usr/bin/python3
"""fetch url"""
import urllib.request

if __name__ == "__main__":
    """work on execution only"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))

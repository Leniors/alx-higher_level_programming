#!/usr/bin/python3
"""HTTPError"""
import sys
import urllib.request
import urllib.error

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.read()
        print(content.decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")

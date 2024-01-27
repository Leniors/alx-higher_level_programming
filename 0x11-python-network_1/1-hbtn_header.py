#!/usr/bin/python3
"""header"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    respo_id = response.getheader('X-Request-Id')
    print(respo_id)

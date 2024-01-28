#!/usr/bin/python3
"""value of 'X-Request-Id' in header"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    """open url"""
    head = response.headers

req_id = head.get('X-Request-Id')
print(req_id)

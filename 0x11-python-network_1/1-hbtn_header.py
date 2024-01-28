#!/usr/bin/python3
"""header"""
import sys
import urllib

with urllib.request.urlopen(sys.argv[1]) as response:
    """open url"""
    head = response.headers
    print(head.get('X-Request-Id'))

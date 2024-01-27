#!/usr/bin/python3
"""header"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    """open url"""
    respo_id = response.getheader('X-Request-Id')
    print(respo_id)

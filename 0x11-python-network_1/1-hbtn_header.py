#!/usr/bin/python3
"""header"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    """open url"""
    respo_id = response.getheader('X-Request-Id')
    print(respo_id)

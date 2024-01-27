#!/usr/bin/python3
"""header"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.getheader("X-Request-Id")
    print(x_request_id)

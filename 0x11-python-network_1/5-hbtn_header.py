#!/usr/bin/python3
"""header"""
import sys
import requests

req = requests.get(sys.argv[1])
print(req.headers.get("X-Request-Id"))

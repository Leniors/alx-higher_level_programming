#!/usr/bin/python3
"""post"""
import sys
import urllib

url = sys.argv[1]
values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    reply = response.read()
    print(reply.decode('utf-8'))

#!/usr/bin/python3
"""Error"""
import sys
import request

if __name__ == "__main__":
    req = request.get(sys.argv[1])
    print(f"Error code: {req.status_code}")

#!/bin/bash
# Display all HTTP methods accepted by the server
curl -sI -X OPTIONS "$1" | grep -i "allow" | awk '{print $2}'

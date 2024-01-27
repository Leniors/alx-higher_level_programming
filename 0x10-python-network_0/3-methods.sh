#!/bin/bash
# Display all HTTP methods accepted by the servera
curl -sI -X OPTIONS $1 | grep -i "Allow:" | awk '{print substr($0, 8)}'

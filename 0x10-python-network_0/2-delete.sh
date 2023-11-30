#!/bin/bash
#delete
curl -s -o /dev/null -w "%{http_code}" -X DELETE "#1"

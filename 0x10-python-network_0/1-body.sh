#!/bin/bash
# body echo -n "${response:0:$((${#response}-4))}"
response=$(curl -s -o /dev/null -w "%{http_code}" $1) && [ $response == 200 ] && echo -n "$(curl -s $1)"

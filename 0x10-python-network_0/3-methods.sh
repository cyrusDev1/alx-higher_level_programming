#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS "$1" -I | grep "Allow:" | cut -d' ' -f 2-

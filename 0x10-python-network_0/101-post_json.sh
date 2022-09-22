#!/bin/bash
# sends a JSON POST request to a URL
curl -sX POST "$1" -d @"$2" -H "Content-Type: application/json"

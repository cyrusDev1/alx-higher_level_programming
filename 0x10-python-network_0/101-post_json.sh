#!/bin/bash
# sends a JSON POST request to a URL
curl -s --json @"$2" "$1"

#!/bin/bash
# displays only the status code of the response.
curl -s -o /dev/null "$1" -w "%{response_code}"

#!/usr/bin/python3
"""that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response."""
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    data = dict()
    data['email'] = sys.argv[2]
    data = urllib.parse.urlencode(data)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode("utf8"))

#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print(content.decode("utf8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

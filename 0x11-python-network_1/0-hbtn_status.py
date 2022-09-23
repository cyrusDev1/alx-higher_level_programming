#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(
            "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".
            format(type(content), content, content.decode("utf8")))

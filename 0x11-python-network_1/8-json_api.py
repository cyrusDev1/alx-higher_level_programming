#!/usr/bin/python3
"""A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    response = requests.post(url, {'q': q})
    try:
        json_content = response.json()
        if json_content == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                json_content.get("id"), json_content.get("name")))
    except Exception:
        print("Not a valid JSON")

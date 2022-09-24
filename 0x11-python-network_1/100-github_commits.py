#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of
the repository"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    name = sys.argv[2]
    url = "https://api.github.com/repos/" + name + '/' + repo + "/commits"
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(0, 10):
            sha = commits[i].get('sha')
            name = commits[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
    except Exception:
        pass

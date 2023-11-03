#!/usr/bin/python3
"""
List 10 commits from recent to oldest of the repository "rails" by "rails".
"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url_argument = "https://api.github.com/repos/{}/{}/commits"\
        .format(owner, repo)
    res = requests.get(url_argument)
    commits_list = res.json()
    for i in range(10):
        print("{}: {}".format(commits_list[i].get('sha'), commits_list[i].
              get('commit').get('author').get('name')))

#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]

    req = requests.get('https://api.github.com/user',
                       auth=(username, password))

    print(req.json().get('id'))

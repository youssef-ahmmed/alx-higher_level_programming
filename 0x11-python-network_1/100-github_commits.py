#!/usr/bin/python3
"""Python script that takes 2 arguments and print all commits by:
    `<sha>: <author name>`"""

import requests
from sys import argv


if __name__ == '__main__':

    repo = argv[1]
    owner = argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url, params={'per_page': 10})

    commits_data = response.json()

    for commit in commits_data:
        sha = commit.get('sha')
        author_name = commit.get('commit', {})\
                            .get('author', {})\
                            .get('name', 'N/A')

        print(f'{sha}: {author_name}')

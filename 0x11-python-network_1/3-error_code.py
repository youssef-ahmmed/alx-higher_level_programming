#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == '__main__':

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except HTTPError as error:
        print(f'Error code: {error.status}')

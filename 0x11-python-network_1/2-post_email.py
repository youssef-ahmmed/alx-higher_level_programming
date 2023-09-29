#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response (decoded in utf-8)"""

import urllib.request
from urllib.parse import urlencode
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urlencode(value).encode("utf-8")

    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode("utf-8"))

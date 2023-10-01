#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter"""

import requests
from sys import argv

if __name__ == '__main__':

    url = "http://0.0.0.0:5000/search_user"
    try:
        q = {'q': argv[1]}
    except IndexError:
        q = {'q': ''}

    try:
        req = requests.post(url, data=q)
        req_dict = req.json()
    except:
        print("Not a valid JSON")
        exit()

    print("No result" if not req_dict
          else f'{[req_dict.get("id")]} {req_dict.get("name")}')

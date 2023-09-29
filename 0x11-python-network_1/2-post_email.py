#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))

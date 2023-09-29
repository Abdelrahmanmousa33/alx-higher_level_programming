#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
  - Displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":

    data = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data)
    print(r.text)

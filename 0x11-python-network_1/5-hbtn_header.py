#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
"""
import sys
import requests

if __name__ == "__main__":

    response = requests.get(sys.argv[1])
    print(response.headers["X-Request-Id"])

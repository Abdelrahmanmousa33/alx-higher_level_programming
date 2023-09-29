#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests

if __name__ == "__main__":

    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": letter}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        r = r.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")

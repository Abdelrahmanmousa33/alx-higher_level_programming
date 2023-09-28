#!/bin/bash
# Takes in a URL, sends a GET request to the URL, displays the body of the response of 200 status code.
curl -s "$1" -L

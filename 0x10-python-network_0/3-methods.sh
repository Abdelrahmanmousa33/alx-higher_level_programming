#!/bin/bash
# sends a DELETE request to the URL and displays the body of a response
curl -sI "$1" | grep "Allow" | cut -d " " -f2-

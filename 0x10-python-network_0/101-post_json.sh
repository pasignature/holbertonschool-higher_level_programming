#!/bin/bash
# sends a JSON POST request and displays the response.
curl -sX POST "$1" -d @"$2" -H "Content-Type: application/json"

#!/bin/bash
# sends a DELETE request to the URL passed as the first argument
curl -sX delete "$1"

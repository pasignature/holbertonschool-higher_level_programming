#!/bin/bash
# displays size of the body of URL response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2

#!/bin/bash
# makes request to 0.0.0.0:5000/catch_me and causes server to respond with message containing You got me!
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
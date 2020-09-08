#!/usr/bin/python3
'''fetches a url and post email using only requests'''
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) == 1:
        let = ""
    else:
        let = argv[1]
    payload = {"q": let}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

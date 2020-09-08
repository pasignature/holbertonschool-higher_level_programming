#!/usr/bin/python3
'''list 10 commits of the repository "rails" by the user "rails"'''
import requests
from sys import argv

if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    res = requests.get(url)
    comm = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                comm[i].get("sha"),
                comm[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

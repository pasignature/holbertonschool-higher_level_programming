## 0x11. Python - Network #1


Resources

Read or watch:

    Quickstart with Requests package
    Requests package

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    How to fetch internet resources with the Python package urllib
    How to decode urllib body response
    How to use the Python package requests #requestsiswaysimplerthanurllib
    How to make HTTP GET request
    How to make HTTP POST/PUT/etc. request
    How to fetch JSON resources
    How to manipulate data from an external service

Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7.*)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
    Your code should not be executed when imported (by using if __name__ == "__main__":)


**0. What's my status? #0**

     Write a Python script that fetches https://intranet.hbtn.io/status

* You must use the package urllib
* You are not allowed to import any packages other than urllib
* The body of the response must be displayed like the following example
  (tabulation before -)
* You must use a with statement

**1. Response header value #0**

     Write a Python script that takes in a URL, sends a request to the URL and
     displays the value of the X-Request-Id variable found in the header of the response.

* You must use the packages urllib and sys
* You are not allow to import packages other than urllib and sys
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a with statement

Andrew Godwin
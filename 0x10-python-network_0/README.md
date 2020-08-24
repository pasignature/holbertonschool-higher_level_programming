## 0x10. Python - Network #0

For this project, students are expected to look at this concept:

    Using cURL to debug

Resources

Read or watch:

    HTTP (HyperText Transfer Protocol) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
    HTTP Cookies

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What a URL is
    What HTTP is
    How to read a URL
    The scheme for a HTTP URL
    What a domain name is
    What a sub-domain is
    How to define a port number in a URL
    What a query string is
    What an HTTP request is
    What an HTTP response is
    What HTTP headers are
    What the HTTP message body is
    What an HTTP request method is
    What an HTTP response status code is
    What an HTTP Cookie is
    How to make a request with cURL
    What happens when you type google.com in your browser (Application level)

Requirements
General

    Allowed editors: vi, vim, emacs
    - A README.md file, at the root of the folder of the project, is mandatory
    All your scripts will be tested on Ubuntu 14.04 LTS
    All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
    All your files should end with a new line
    All your files must be executable
    The first line of all your bash files should be exactly #!/bin/bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing
    All curl commands must be have the option -s (silent mode)
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    The first line of all your Python files should be exactly #!/usr/bin/python3
    Your code should use the PEP 8 style (version 1.7.*)
    All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
    All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'


**0. cURL body size**
     Write a Bash script that takes in a URL, sends a request to that URL,
     and displays the size of the body of the response

* The size must be displayed in bytes
* You have to use curl
* Please test your script in the container provided, using the web server
  running on port 5000

**1. cURL to the end mandatory**

     Write a Bash script that takes in a URL, sends a GET request to the URL,
     and displays the body of the response

* Display only body of a 200 status code response
* You have to use curl
* Please test your script in the container provided, using the web server
  running on port 5000

**2. cURL Method mandatory**

     Write a Bash script that sends a DELETE request to the URL passed as the
     first argument and displays the body of the response

* You have to use curl
* Please test your script in the container provided, using the web server
  running on port 5000
  
  Andrew Godwin
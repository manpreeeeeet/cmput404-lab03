#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page,after_login_incorrect, _wrapper

import os
import json

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

print("Content-Type: text/html")
print()

if not username and not password:
    print(login_page)


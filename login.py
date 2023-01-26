#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page,after_login_incorrect, _wrapper

import os
import json
import secret
from http.cookies import SimpleCookie


cookies = SimpleCookie(dict(os.environ)["HTTP_COOKIE"])



s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

print("Content-Type: text/html")
if username == secret.username and password == secret.password:
    print("Set-Cookie: password=" + password)
    print("Set-Cookie: username=" + username)
print()

logged_in = False
if cookies.get("username") is not None and cookies.get("password") is not None:
    if cookies.get("username").value == secret.username and cookies.get("password").value == secret.password:
        logged_in = True 



if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password,logged_in))
else:
    print(after_login_incorrect())

print()

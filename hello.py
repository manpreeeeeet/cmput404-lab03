#!/usr/bin/env python3

import os
import json

from templates import login_page, secret_page,after_login_incorrect, _wrapper
print("Content-Type: text/html")
print()
print(json.dumps(dict(os.environ,indent = 2)))
#print(_wrapper(os.environ["QUERY_STRING"]))
#print(_wrapper(os.environ["HTTP_USER_AGENT"]))
print()



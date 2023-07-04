#!/usr/bin/python3

from urllib import request


url = 'https://alx-intranet.hbtn.io/status'
res = None

with request.urlopen(url) as response:
    res = response.read()

res_type = type(res)
res_utf8_content = res.decode('utf-8')

print(f'''Body response:
\t- type: {res_type}
\t- content: {res}
\t- utf8 content: {res_utf8_content}''')

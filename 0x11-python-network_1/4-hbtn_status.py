#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import requests

url = 'https://alx-intranet.hbtn.io/status'
res = requests.get(url)
content = res.text

print(f'''Body response:
\t- type: {type(content)}
\t- content: {content}''')

#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)"""

if __name__ == '__main__':
    import sys
    from urllib import request, parse

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    data = parse.urlencode(data)
    data = data.encode('ascii')

    req = request.Request(url, data)

    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

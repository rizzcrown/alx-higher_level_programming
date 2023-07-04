#!/usr/bin/python3
"""sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""

if __name__ == '__main__':
    import sys
    from urllib import request

    url = sys.argv[1]

    with request.urlopen(url) as response:
        meta = response.info()
        for header in meta._headers:
            if header[0] == 'X-Request-Id':
                print(header[1])

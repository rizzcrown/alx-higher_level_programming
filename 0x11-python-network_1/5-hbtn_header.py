#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header"""

if __name__ == '__main__':
    import sys
    from requests import get

    url = sys.argv[1]
    res = get(url)

    print(res.headers.get('X-Request-Id'))

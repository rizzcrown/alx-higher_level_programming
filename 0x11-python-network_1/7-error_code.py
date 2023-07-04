#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response."""

if __name__ == '__main__':
    import sys
    from requests import get, codes

    url = sys.argv[1]
    res = get(url)

    if res.status_code != codes.ok:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)

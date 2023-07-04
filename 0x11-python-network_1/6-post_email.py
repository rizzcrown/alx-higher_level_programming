#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter and finally displays the body of the response"""

if __name__ == '__main__':
    import sys
    from requests import post

    url = sys.argv[1]
    email = sys.argv[2]

    res = post(url, data={'email': email})
    print(res.text)

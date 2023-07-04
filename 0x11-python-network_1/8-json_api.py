#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == '__main__':
    import sys
    from requests import post, codes

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    query = {'q': q}
    res = post(url, data=query)

    if res.status_code != codes.ok or len(res.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            my_obj = res.json()
            if len(my_obj) == 0:
                print('No result')
                sys.exit()
            my_id = my_obj.get('id')
            my_name = my_obj.get('name')
            print("[{}] {}".format(my_id, my_name))
        except ValueError as invalid_json:
            print('Not a valid JSON')

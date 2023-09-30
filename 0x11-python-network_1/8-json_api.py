#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


def main(av):
    import requests

    if len(av) == 2:
        letter = av[1]
    else:
        letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    resp = requests.post(url, data=data)
    json_data = resp.json()

    if json_data != None:
        print("[<{}>] <{}>".format(json_data["id"], json_data["name"]))
    else:
        print('No result')


if __name__ == '__main__':
    from sys import argv
    main(argv)

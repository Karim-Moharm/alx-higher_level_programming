#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
the body of the response
"""


def main(av):
    import requests
    resp = requests.get(av[1])
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)


if __name__ == '__main__':
    from sys import argv
    main(argv)

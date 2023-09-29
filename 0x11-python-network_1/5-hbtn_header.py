#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""


def main(av):
    """main function
    """
    import requests
    resp = requests.get(av[1], auth=('user', 'pass'))

    if resp.status_code == 200:
        print(resp.headers['X-Request-Id'])


if __name__ == '__main__':
    from sys import argv
    main(argv)

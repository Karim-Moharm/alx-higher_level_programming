#!/usr/bin/python3
"""sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""


def main(av):
    import urllib.request
    url = av[1]

    with urllib.request.urlopen(url) as resp:
        if 'X-Request-Id' in resp.headers:
            x_req_id = resp.headers['X-Request-Id']
            print(x_req_id)


if __name__ == '__main__':
    from sys import argv
    main(argv)

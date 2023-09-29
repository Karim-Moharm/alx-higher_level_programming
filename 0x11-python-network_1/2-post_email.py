#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""


def main(av):
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    import urllib.request

    url = av[1]
    email = av[2]
    req = urllib.request.Request(url, email)

    try:
        with urlopen(url) as resp:
            resp_body = resp.read().decode('UTF-8')
            print(resp_body)
    except URLError as e:
        print(str(e))
    except HTTPError as e:
        print(e.code)


if __name__ == '__main__':
    from sys import argv
    main(argv)

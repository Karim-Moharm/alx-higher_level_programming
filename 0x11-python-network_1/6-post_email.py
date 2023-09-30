#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally
displays the body of the response
"""


def main(av):
    import requests

    url = av[1]
    email = av[2]
    data = {'email': email}

    resp = requests.post(url, data=data)
    print(resp.text)


if __name__ == '__main__':
    from sys import argv
    main(argv)

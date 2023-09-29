#!/usr/bin/python3
"""takes URL and display the body of the responce with error handling
"""


def main(av):
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.error import URLError

    try:
        with urlopen(av[1]) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    except URLError as e:
        print(str(e))


if __name__ == '__main__':
    from sys import argv
    main(argv)

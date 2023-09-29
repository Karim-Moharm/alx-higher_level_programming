#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""


def main(av):
    """main function
    """
    import urllib.request
    import urllib.parse
    url = av[1]
    email = av[2]

    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            utf8_content = response.read().decode('utf-8')
            print(utf8_content)

    except urllib.error.HTTPError as e:
        print("HTTP Error: ", e.code)
    except urllib.error.URLError as e:
        print("URL Error: ", e.reason)
    except Exception as e:
        print("An error: ", str(e))


if __name__ == '__main__':
    from sys import argv
    main(argv)

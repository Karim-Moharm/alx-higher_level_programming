#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""


def main():
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url, auth=('user', 'pass'))
    print('Body response:')
    print('\t- type: {}'.format(type(resp.text)))
    print('\t- content: {}'.format(resp.text))


if __name__ == '__main__':
    main()

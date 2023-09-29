#!/usr/bin/python3
"""python script that fetches https://alx-intranet.hbtn.io/status
"""


def main():
    """main function
    """
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read()

    # print(dir(data))

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode("UTF-8")))


if __name__ == "__main__":
    main()

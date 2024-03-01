#!/usr/bin/python3
"""A script that get status code
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        title = "Body response:"
        second_line = "\t- type: {}".format(type(content))
        third_line = "\t- content: {}".format(content)
        last_line = "\t- utf8 content: {}".format(content.decode('utf-8'))
        print(title)
        print(second_line)
        print(third_line)
        print(last_line)

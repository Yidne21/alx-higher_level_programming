#!/usr/bin/python3
"""This script Fetches the URL: https://intranet.hbtn.io/status"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request('https://intranet.hbtn.io/status')

    with urlopen(req) as res:
        content = res.read()
        utf8_content = content.decode('utf-8')
        _type = type(content)
        _content = content
        _utf8_c = utf8_content

        print('Body response:')
        print('\t- type: {}'.format(_type))
        print('\t- content: {}'.format(_content))
        print('\t- utf8 content: {}'.format(_utf8_c))

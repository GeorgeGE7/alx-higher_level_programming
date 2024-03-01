#!/usr/bin/python3
"""A script that: get eror code from url
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res_body:
            print(res_body.read().decode('UTF-8'))
    except error.HTTPError as errror:
        print('Error code:', errror.code)

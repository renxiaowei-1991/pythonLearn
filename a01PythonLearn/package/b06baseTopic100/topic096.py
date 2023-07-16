#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def requests_test():
    url = "http://antpython.net/"
    print("requests.models: ", requests.models)

    print("请求: ", type(requests.Request()))
    print(requests.Request(url))

    print("相应: ", type(requests.Response()))
    print(requests.get(url))



    req = requests.get("http://antpython.net/")
    print(req.url)
    print(req.text)


if __name__ == "__main__":
    requests_test()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import webbrowser

import requests
import os


def requests_test():
    """
    获取网页内容
    """
    url = "http://antpython.net/"
    print("requests.models: ", requests.models)

    print("请求: ", type(requests.Request()))
    print(requests.Request(url))

    print("响应: ", type(requests.Response()))
    print(requests.get(url))

    req = requests.get("http://antpython.net/")
    print("url: ", req.url)
    print(req.text)
    return


def requests_test_1():
    """
    获取网络文件
    :return:
    """
    url_file = "http://antpython.net/static/py100/life_is_great.txt"
    req = requests.get(url_file)
    # 文件信息
    print(req.headers)
    # 返回码
    print(req.status_code)
    # url
    print(req.url)
    # 文件内容
    print(req.text)
    return


def requests_test_2():
    """
    获取网络图片
    req.content 二进制格式
    req.text 文本格式
    :return:
    """
    url_file = "http://antpython.net/static/pubdatas/webspider/goodimgs/9.jpeg"
    file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\picture\\"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    # 获取图片文件
    req = requests.get(url_file)
    print("文件头(字典): ", type(req.headers))
    # 获取文件名: 解析文件头
    filename = dict(req.headers)["Content-Disposition"].split("=")[1]
    # 使用二进制将图片内容保存到图片文件中
    with open(file_path + filename, "wb+") as f:
        # req.content 二进制格式
        # req.text 文本格式
        f.write(req.content)
    return


def requests_test_3():
    url_file = "http://antpython.net/static/pubdatas/webspider/goodimgs/*"
    file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\picture\\"
    print(requests.get(url_file).headers)
    return


def requests_test_4():
    """
    通过python给网页提交数据
    :return:
    """
    url = "http://antpython.net/webspider/grade_form"
    param = {
        "sname": "任末",
        "yuwen": 100,
        "shxue": 99,
        "yingyu": 98
    }
    # 用requests，使用post方式，向url请求，传输的数据是param，格式是json字符串
    resp = requests.post(url, data=param)
    print(resp)
    return


def requests_test_5():
    """
    使用默认浏览器，使用百度搜索指定关键词，并打开浏览器
    :return:
    """
    url = "https://www.baidu.com/s?wd=python"
    # 使用默认浏览器，使用百度搜索指定关键词，并打开浏览器
    query = input("请输入搜索词: ")
    # webbrowser.open(url.replace("python", input("请输入搜索词: ")))
    webbrowser.open(f"https://www.baidu.com/s?wd={query}")
    return


if __name__ == "__main__":
    # requests_test()
    # requests_test_1()
    # requests_test_2()
    # requests_test_3()
    # requests_test_4()
    requests_test_5()
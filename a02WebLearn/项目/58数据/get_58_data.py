#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv


def get_data():
    url = "https://bj.58.com/chaoyang/chuzu/?key=租房&final=1&PGTID=0d3090a7-0047-758d-02c9-16424e52ab36&ClickID=2"
    param = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    response = requests.get(url, params=param)
    bs = BeautifulSoup(response.text, 'html.parser')
    print(bs.find_all())


if __name__ == '__main__':
    get_data()
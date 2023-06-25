#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import sys


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)
print("Content-type:text/html")
print()
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>Hello World - 我的第一个 CGI 程序！</title>')
print('</head>')
print('<body>')
print('<h2>Hello World! 我是来自菜鸟教程的第一CGI程序</h2>')
print('</body>')
print('</html>')
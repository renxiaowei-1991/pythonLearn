#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import sys

"""
CGI
    CGI目前由NCSA维护，NCSA定义CGI如下：
    CGI(Common Gateway Interface)，通用网关接口，它是一段程序，运行在服务器上，如：HTTP服务器，提供同客户端HTML页面的接口

网页浏览
    为了更好的了解CGI是如何工作的，可以从页面点击一个链接或URL的流程开始：
    1、使用浏览器范文URL并链接到HTTPweb服务器
    2、Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容，否则返回错误信息
    3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息

CGI程序
    CGI程序可以是Python脚本，PERL脚本，SHELL脚本，C或者C++程序等

CGI编程
    1、需要先在目录下执行开启服务的语句 
        目录是存放cgi-bin文件夹的目录。相当于tomcat存放服务的地方
        进入存放cgi-bin目录的地方，一般是./www。执行语句。
        python -m http.server --cgi 8001
        并且这个服务得一直开的，DOS窗口不用关
        CGI脚本存放在 cgi-bin 目录中
    2、在pycharm配置debug配置
    3、浏览器
        http://localhost:8001/cgi-bin/cgiTest.py

"""

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

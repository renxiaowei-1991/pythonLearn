#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
python爬虫开发

简单爬虫架构
    爬虫调度端(启动、停止)
    爬虫架构(三大模块)
        URL管理器：URL队列管理，防止重复爬取，支持新增URL和取出URL
            数据容器，存放待爬取和爬取过的URL。网页相互之间的链接非常复杂，如果不对URL进行管理，会进行循环爬取，重复爬取，导致死循环
        网页下载器：网页内容下载
        网页解析器：提取价值数据，提取新的待爬URL
    价值数据：数据存储，数据分析

URL管理器
    对爬取URL进行管理，防止重复和循环爬取，支持新增URL和取出URL
    1) 对外接口：取出一个待爬取URL；新增待爬取URL
    2) 实现逻辑：取出时，状态变成已爬取；新增时，判断URL是否已经存在。逻辑可以进行优化
    3) 数据存储：
        Python内存：待爬取URL集合：set；已爬取URL集合：set
        redis(NoSQL)：待爬取URL集合：set；已爬取URL集合：set
        MySQL：urls(url, is_crawled)

requests: 网页下载
    Requests是一个优雅的、简单的Python HTTP库，常用于爬虫中对网页内容的下载。
    Python程序: 通过requests库，向网页服务器，发送一个request请求，请求中包含了想要访问的URL、属性、Cookies等
    网页服务器：会对request请求进行解析，将结果通过response对象放回给Python程序。Response对象里面包含了要提取的网页的内容以及各种附带属性

    requests.get/post(url, params, data, headers, timeout, verify, allow_redirects, cookies)
        get/post: 请求方法
        url: 要下载的目标网页的URL
        params: 字典形式，设置URL后面的参数，比如?id=123&name=xiaoming
        data: 字典或者字符串，一般用于POST方法时提交数据
        headers: 设置user-agent、refer等请求头
        timeout: 超时时间，单位是秒
        verify: True/False, 是否进行HTTPS证书验证，默认是，需要自己设置证书地址
        allow_redirects: True/False是否让requests做重定向处理，默认是
        cookies: 附带本地的cookies数据。如果网站需要登录，cookies是网站登录后保存在客户端本地的状态码，请求的时候带上cookies可以用于保持登录。

        注意：
            如果headers里面什么都没有，会被认为是爬虫。可以在headers里面加一下内容，伪装成一个正常的网页

    接收response响应。提取内容。
        r = requests.get/post(url)
        r.status_code : 查看状态码
        r.encoding : 查看当前编码以及变更编码(requests会根据Headers推测编码，推测不到则设置为ISO=8859-1，可能导致乱码)
            如果有乱码，需要查看网页源代码，查看编码格式。然后手动修改response的encoding
            r.encoding="utf-8"
        r.headers : 查看返回的HTTP的headers
        r.url : 查看实际访问的URL。可能和访问的URL不一致
        r.text : 查看返回的网页内容。可能是Html,json...
        r.content : 以字节的方式返回内容，比如用于下载图片。将二进制数据写入到图片中，就是想要下载的图片
        r.cookies : 服务端要写入本地的cookies数据

beautifulsoup4/bs4: 网页解析
    注意：安装的时候安装beautifulsoup4，导入的时候导入bs4.BeautifulSoup
    Python第三方库，用于从HTML中提取数据
    导入:
        import bs
        from bs4 import BeautifulSoup

    解析网页文本，提取内容，有各种不同方式。
        正则表达式。但是正则表达式，提取比较乱的网页的时候，非常困难，会有很多格式化的问题。
        BeautifulSoup比较方便

    使用方式：
        获取Html网页
        创建BeautifulSoup对象
        搜索节点find_all(查找一系列节点),find(查找第一个节点)
            按节点名称: html标签
            按节点属性值: html属性
            按节点文字: html标签显示值(标签中间部分)
        访问节点:名称,属性,文字
        注意：
            搜索以后的结果是<class 'bs4.element.Tag'>。可以继续被搜索
            一般为了精确查找，都是先查找一个子标签出来，再基于子标签进行搜索，能更快速和精确的定位数据

    代码样式：
        # 对象创建
        soup = BeautifulSoup(html_doc, # HTML文档字符串
                            'html.parser', # HTML解析器
                            from_encoding='utf8' # HTML文档的编码
                            )
        # 搜索节点
        # find_all(name, attrs, string)
        #     name: 节点名称
        #     attrs: 节点属性
        #     string: 节点文字
        soup.find_all('a') # 查找所有标签为a的节点
        soup.find_all('a', href='/view/123.html') # 查找所有标签为a，链接符合/view/123.html形式的节点
        soup.find_all('div', class_='abc', string='python') # 查找所有标签为div，class为abc，文字为Python的节点
            # 这里的class需要加下划线，因为和python关键字冲突了

        # 得到节点: <a href="1.html">Python</a>
        node.name # 获取查找到的节点的标签名称
        node['href'] # 获取查找到的a节点的href属性
        node.get_text() # 获取查找到的a节点的链接文字



Selenium: 自动化测试模块，动态网页下载
    实现浏览器自动化操作<模拟人的行为操作浏览器>

    正常手动浏览器网站获取数据
    1、打开浏览器
    2、访问网站
    3、输入关键字，进行搜索
    4、浏览商品数据

    selenium操作浏览器
    1、打开浏览器
        - 谷歌浏览器
        - 谷歌驱动安装
            1、查看浏览器版本 115.0.5790.171
            2、下载浏览器驱动，选择和浏览器版本最相近的版本即可。 114.0.5735.90
                https://registry.npmmirror.com/binary.html?path=chromedriver/
            3、驱动文件解压之后，将驱动放到python安装目录
                - 将驱动的.exe放到python安装目录即可。目的是把.exe所在目录加到path环境变量。放到python安装目录也能实现相同的功能
                - 创建一个目录，将.exe驱动文件放到目录中，把该目录添加到path环境变量中
                - 或者把加压后的文件夹放在python安装目录，然后把该文件夹路径添加到path中
                    E:\02-helloWorld\03Python\chromedriver_win32
    2、访问网站
    3、输入关键字，进行搜索
        元素定位，定位到浏览器相应位置，进行操作
        鼠标点击搜索
            from selenium.webdriver import ActionChains
        键盘回车搜索
            from selenium.webdriver.common.keys import Keys
    4、浏览商品数据
        获取数据如果为空列表，有两种情况。
        - 语法错误
        - 网页数据还没有加载出来

    网络加载等待：设置延时等待
        driver.implicitly_wait(10): 弱等待，网页加载完成后就不等待了
        time.sleep(10): 强等待，不管是否加载完成，都需要等待10秒

    函数(4.*版本已弃用)：
        find_element_by_id
        find_element_by_name
        find_element_by_xpath
        find_element_by_link_text
        find_element_by_partial_link_text
        find_element_by_tag_name
        find_element_by_class_name
        find_element_by_class_selector

        find_elements_by_id
        find_elements_by_name
        find_elements_by_xpath
        find_elements_by_link_text
        find_elements_by_partial_link_text
        find_elements_by_tag_name
        find_elements_by_class_name
        find_elements_by_class_selector

    4.*版本函数
        find_element: 返回一个元素
        find_elements: 返回一个列表

    from selenium.webdriver.common.by import By
        获取元素的方法类型
    from selenium.webdriver.common.keys import Keys
        控制键盘
    from selenium.webdriver import ActionChains
        控制鼠标
        ActionChains执行原理：当调用ActionChains的方法是，不会立即执行，而是会将所有的操作按顺序存放在一个队列里，当调用perform()方法是，队列中的事件会依次执行

    问题：
        打开浏览器闪退：
        版本问题：
            selenium版本太高
                依次从高版本到低版本测试，哪个版本可以使用。我的是4.0.0
            驱动版本和浏览器版本差别太大
                选择最接近的版本即可
                https://registry.npmmirror.com/binary.html?path=chromedriver/

        驱动位置问题
            - 将驱动的.exe放到python安装目录即可。目的是把.exe所在目录加到path环境变量。放到python安装目录也能实现相同的功能
            - 创建一个目录，将.exe驱动文件放到目录中，把该目录添加到path环境变量中

        driver变量范围问题
            1、不设置driver为全局，放在函数内(会闪退)
            2、把driver放在函数外，为全局(不会闪退)
            3、把driver放在函数内，设置为全局(不会闪退)

        注意：
            如果浏览器更新后，可能需要更新驱动版本。


爬虫开发步骤

Google Chrome浏览器

    查看网页源代码
        显示的是没有执行js代码的源代码，可以通过html格式化工具进行格式
    检查
        可以通过设置，将检查显示在浏览器下方
        Elements:
            显示的是执行了js之后的源代码，可能已经进行了一些动态脚本。
            获取执行js之后的动态网页的方法是使用Selenium插件。
            Selenium就是模拟浏览器，真正下载html，执行javascript。把最终真正用户看到的内容呈现出来。

            Elements可以定位一段显示对于的源代码的位置。在上面网页上面找到显示内容，右键-检查。就会直接定位到对应的源代码

        Network: 抓包
            刷新页面，会显示网页加载的时间，和网页性能
            会显示加载的子URL，JS，以及访问的内容

            Preserve log: 如果跨网站访问，选择了则个功能，日志会一直保存，不会丢失。如果不点，到了新的网页，日志就会进行刷新，不会保留上一个网页的日志。
            Disable cache: 爬虫的时候需要选择。否则可能会从本地取数据。爬取的结果可能会和表现的不一致
            Doc/JS/CSS/Img/Media/Font/Doc: 这些选择可以设置Network获取到的网站内容的显示选项
            Name: 加载的网站内容。例如：网站/css/js/img/...  点击其中一项后，在右边会显示具体内容
                Headers: 网页请求头。用于设置向网站传输的内容。
                Preview:
                Response: 相应内容
                Cookies:
                Timing:

"""
import time

"""
Web知识

HTTP请求协议(B-->S):request(包含4部分)
    1、请求行: 包含三部分
        1) 请求方式(7种)
            get
            post
            delete
            put
            head
            options
            trace
        2) URI:统一资源标识符
            URI: 统一资源标识符。代表网络中某个资源的名字。但是通过URI无法定位资源
            URL: 统一资源定位符。代办网络中某个资源，通过URL可以定位到该资源
            URL包括URI
            样例:
                URL: localhost:8080/servlet0...
                URI: /servlet05/index.html
        3) HTTP协议版本号
    2、请求头
        请求的主机
        主机的端口
        浏览器信息
        平台信息
        cookies等信息
        ...
    3、空白行
        空白行用来区分 请求头 和 请求体
    4、请求体
        向服务器发送的具体数据

HTTP响应协议(S-->B):response(包含4部分)
    1、状态行：包含三部分
        1) 协议版本好(HTTP/1.1)
        2) 状态码：HTTP协议中规定的响应状态号。不同的响应结果对应不同的号码
            200：请求响应成功，正常结束
            404：表示访问的资源不存在。404错误是前端错误
            405：表示前端发送的请求方式与后端请求的处理方式不一致
                例如：前端是POST请求，后端的处理方式按照GET方式进行处理
            500：服务器端的程序出现异常。一般会认为是服务器端的错误导致的。
            注意：
                以4开头的，一般是浏览器端的错误导致的
                以5开头的，一般是服务器端的错误导致的
        3) 状态的描述信息
            ok: 表示正常成功结束
            not found: 表示资源找不到

    2、响应头
        响应的内容类型
        响应的内容长度
        响应的时间
        ...

    3、空白行
        用来分割 响应头 和 响应体

    4、响应体
        响应体就是响应的正文，这些内容是一个长的字符串，这个字符串被浏览器渲染，解释并执行，最终展示出效果


"""

"""
ipython测试样例
ipython安装
    python -m pip install ipython

import requests
url = "http://www.crazyant.net"
r = requests.get(url)
r.status_code
r.headers
r.encoding
r.text
r.cookies
history
url = "http://www.baidu.com"
r = requests.get(url)
r.status_code
r.headers
r.encoding
r.text
r.encoding="utf-8"
r.text
url = "http://www.httpcn.com"
r = requests.get(url)
r.status_code
r.encoding
r.headers
r.text
r.encoding="utf-8"
r.text
history
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# 获取元素的类型
from selenium.webdriver.common.by import By
# 控制键盘
from selenium.webdriver.common.keys import Keys
# 控制鼠标
from selenium.webdriver import ActionChains


def beautifulsoup_test():
    # 打开本地html，获取html内容
    html_file_path = r"D:\02helloWorld\03Python\a02WebLearn\pkg\web\html"
    with open(html_file_path + "/test01.html", 'r+', encoding="utf-8") as fin:
        html_doc = fin.read()

    # 通过获取到的本地html内容创建Beautifulsoup对象
    soup = BeautifulSoup(html_doc, "html.parser")
    print(type(soup))
    links = soup.find_all('a')
    for link in links:
        print(link)
        print(type(link))
        print(link.name, link['href'], link.get_text())
    img = soup.find('img')
    print(img["src"])
    print("#"*30)

    # 先定位到目标块，再从目标块中获取数据
    # <class 'bs4.element.Tag'>可以继续被搜索
    div_node = soup.find('div', id="content")
    print(div_node)
    print(type(div_node))
    links = div_node.find_all('a')
    for link in links:
        print(link.name, link["href"], link.get_text())


def selenium_test():
    # 1、打开浏览器(加载驱动)
    # 处理浏览器闪退问题
    #   1、不设置driver为全局，放在函数内(会闪退)
    #   2、把driver放在函数外，为全局(不会闪退)
    #   3、把driver放在函数内，设置为全局(不会闪退)
    global driver
    driver = webdriver.Chrome()
    # 浏览器设置全屏
    driver.maximize_window()
    # 2、访问网站
    driver.implicitly_wait(5)
    driver.get("https://www.jd.com/")
    # 3、输入关键词
    #   元素定位，定位到浏览器相应位置，进行操作
    driver.find_element(by=By.ID, value='key').send_keys('口红')
    # 4、进行搜索
    #   1) 鼠标点击搜索
    # 获取想要点击的元素
    element = driver.find_element(by=By.XPATH, value='//*[@id="search"]/div/div[2]/button/i')
    # 实例化鼠标操作
    # ActionChains执行原理：当调用ActionChains的方法是，不会立即执行，而是会将所有的操作按顺序存放在一个队列里，当调用perform()方法是，队列中的事件会依次执行
    action = ActionChains(driver)
    # action.move_to_element(element)
    # 左键点击鼠标
    action.click(element)
    # 提交鼠标实例上面的所有操作
    action.perform()
    print(element)
    #   2) 键盘回车搜索
    # driver.find_element(by=By.ID, value='key').send_keys(Keys.ENTER)
    print(driver)
    # 4、获取商品数据
    #   - 找到商品对应标签位置
    #   - 需要等待页面加载完成，设置延时等待，加载完成之后就执行下面的代码
    driver.implicitly_wait(10)
    shops = driver.find_elements(by=By.CLASS_NAME, value='gl-i-wrap')
    for shop in shops:
        # 通过css选择器获取具体的内容
        title = shop.find_element(by=By.TAG_NAME, value='.p-name a em')
        print(title)
    # print(shops)

    return


# beautifulsoup_test()
selenium_test()

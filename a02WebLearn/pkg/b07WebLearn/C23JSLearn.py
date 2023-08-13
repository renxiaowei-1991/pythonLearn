#!/usr/bin/env python
# -*- coding:utf -*-

"""
HTTP协议
    W3C指定的一种超文本传输协议(通信协议：发送消息的模板提前被定制好)
    HTTP协议包括：
        请求协议：浏览器向WEB服务器发送数据的时候，这个发送的数据需要遵循一套标准，这套标准中规定了发送的数据具体格式。
        响应协议：WEB服务器向浏览器发送数据的时候，这个发送的数据需要遵循一套标准，这套标准中规定了发送的数据具体格式
    HTTP协议就是提前制定好的一种消息模板

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

GET&POST选择
    到目前为止，只有一种请求发送POST请求：使用form表单，并且form标签中的method属性值为：method="post"。其他所有情况一律都用get请求

    GET：从服务器获取数据
    POST：向服务器传输数据

GET&POST区别
    get请求在"请求行"上发送数据：get请求发送数据的时候，数据会挂在URI的后面，并且在URI后面添加一个"?"，"?"后面是数据。这样会导致发送的数据回显在浏览器的地址栏上。
    post请求在"请求体"当中发送数据：post请求发送数据的时候，在请求体当中发送。不会回显到浏览器的地址栏也就是说post发送的数据，在浏览器地址栏上看不到。

    get请求只能发送普通的字符串。并且发送的字符串长度有限制，不同的浏览器限制不同。
    get请求无法发送大数据量
    post请求可以发送任何类型的数据，包括普通字符串，流媒体等信息：视频、声音、图片。
    post请求可以发送大数据量，理论上没有长度限制
    get请求在W3C中是这样说的：get请求比较适合从服务器端获取数据
    post请求在W3C中是这样说的：post请求比较适合向服务器端传送数据

    get请求是安全的。get请求只是为了从服务器上获取数据。不会对服务器造成威胁。
    post请求是危险的。post请求是向服务器提交数据，如果这些数据通过后门的方式进入到服务器当中，服务器是很危险的。另外post是为了提交数据，所以一般情况下拦截请求的时候，大部分会选择拦截(监听)post请求

    get请求支持缓存。任何一个get请求最终的”响应结果“都会被浏览器缓存起来。发送get请求的时候，浏览器首先会从本地浏览器缓存中查找，找不到再去服务器查找。
        如果不想在本地缓存找，每次都想要在服务器找。可以每次都修改get请求路径即可。例如加个时间戳。get请求路径不同，就不会走缓存了
    post不支持缓存。服务器”响应结果“不会被浏览器缓存。因为没有意义。

W3C
    万维网联盟组织
    负责制定标准的：HTTP HTML4.0 HTML5.0 XML DOM等规范都是W3C制定的

超文本
    不是普通文本，比如流媒体：声音、视频、图片等
    HTTP协议支持：不但可以传送普通字符串，同样支持传递声音、视频、图片等流媒体信息。
    这种协议游走在B和S之间。B向S发送数据要遵循HTTP协议。S向B发送数据同样要遵循HTTP协议。


"""
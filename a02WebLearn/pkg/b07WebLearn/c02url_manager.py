#!/usr/bin/env python
# -*- coding:utf-8 -*-

class UrlManager():
    """
    爬虫-URL管理器实现
    """
    def __init__(self):
        """
        初始化URL管理器
            new_urls: 存放未爬取URL和新增URL
            old_ursl: 存放已爬取URL
        """
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        新增待爬取URL
        :param url:
        :return:
        """
        if url is None or len(url) == 0:
            return
        elif url in self.new_urls or url in self.old_urls:
            return
        else:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        批量添加待爬取URL
        :param urls:
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        else:
            for url in urls:
                self.add_new_url(url)

    def get_url(self):
        """
        获取一个待爬取URL
        :return:
        """
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        """
        判断一个URL是否是一个待爬取URL
        :param url:
        :return:
        """
        return len(self.new_urls) > 0


if __name__ == "__main__":
    url_manager = UrlManager()
    url_manager.add_new_url("url1")
    url_manager.add_new_urls(["url1", "url2"])
    print(url_manager.new_urls, url_manager.old_urls)

    print("#"*30)
    print(url_manager.get_url())
    print(url_manager.new_urls, url_manager.old_urls)

    print("#"*30)
    print(url_manager.get_url())
    print(url_manager.new_urls, url_manager.old_urls)

    print("#"*30)
    print(url_manager.has_new_url())

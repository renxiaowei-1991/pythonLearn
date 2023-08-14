#!/usr/bin/env pyton
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import csv


def get_date():
    """
    获取京东商品数据
    :return:
    """
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
    goods = driver.find_elements(by=By.CLASS_NAME, value='gl-i-wrap')
    data = []
    for good in goods:
        # 通过css选择器获取具体的内容
        # .p-name class
        # .p-name下面的子标签a
        # a下面的子标签em
        try:
            title = good.find_element(by=By.TAG_NAME, value='.p-name a em').text
            price = good.find_element(by=By.TAG_NAME, value='.p-price strong i').text
            comment = good.find_element(by=By.TAG_NAME, value='.p-commit strong a').text
            shop = good.find_element(by=By.TAG_NAME, value='.p-shop span a').text
            dic = {
                '标题': title,
                '价格': price,
                '评论': comment,
                '店铺': shop
            }
            data.append(dic)
        except BaseException as be:
            print("异常")
    print(data)
    return data


def save_data(data):
    with open('./data.csv', 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=[
            '标题', '价格', '评论', '店铺'
        ])
        # 写入表头
        csv_writer.writeheader()
        csv_writer.writerows(data)
    print("文件写入完成")
    return


if __name__ == "__main__":
    save_data(get_date())

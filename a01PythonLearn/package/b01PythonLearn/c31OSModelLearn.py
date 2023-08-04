#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import datetime
import time
import zipfile



"""
    os模块
    
    环境变量
        环境变量是程序和操作系统之间的通信方式。有些字符不宜明文写进代码里，比如数据库密码，个人账户密码。如果写进自己本机的环境变量中，程序用的时候通过os.environ.get()取出来就行。
        这样开发人员本机测试的时候用的是自己本机的一套密码，生产部署的时候，用的是公司的公共账号和密码，这样就能增加安全性。
    
    os.name
        获取当前操作系统名称
        
    os.environ
        获取当前系统的环境变量
    
    os.environ.get('key', default = None)
        获取环境变量的方法
        os.environ是一个字典，是环境变量的字典。如果有可key对应的环境变量，则返回环境变量。如果不存在，默认返回None，可以指定返回值。
        os.environ.get(key, "未找到环境变量")
    
    os.getenv(key, default = None)
        获取环境变量的方法
        如果不存在，默认返回None，可以指定返回值。
        os.getenv(key, "未找到环境变量")
        os.getenv ==(等价于) os.environ.get
        os.getenv 底层调用的也是 os.environ.get
        
    os.sep
        获取当前操作系统的系统路径分隔符
        
    os.linesep
        获取当前操作系统的行分隔符
    
    
    
    os.getcwd()
        获取当前工作目录
        
    os.chdir()
        改变当前工作目录
        如果路径中有中文，则在路径前面加'r'
        
    os.makedir()
        创建目录，可以创建多级目录
    
    os.mkdir()
        创建目录，只能创建单级目录
        如果创建路径中，多级路径不存在会报错；如果创建的单级路径已存在，会报错。
        
    os.removedirs()
        可递归删除空目录，一定都是空目录才能删除
        
    os.rmdir()
        删除单级空目录
        
    os.listdir()
        列出当前目录下的文件夹、文件、隐藏文件
        
    os.remove()
        删除文件
        
    os.rename()
        重命名文件和文件夹
        
    os.stat(filename)
        获取文件或者文件夹信息
        
        
    
    os.path.abspath()
        获取文件或文件夹绝对路径
        
    os.path.split()
        将路径分割成文件或者文件夹组成的二元组
        如果文件夹为空，则返回空字符串、文件夹二元组
    
    os.path.dirname()
        返回的是路径中的目录名，可以看做是split分割后的第一个元素
        
    os.path.basename()
        返回的是路径中的文件名，可以看做是split分割后的第二个元素
        
    os.path.exists()
        判断文件夹、文件是否存在。
        
    os.path.isabs()
        判断是否是绝对路径
        
    os.path.isfile()
        判断是否是文件
        
    os.path.isdir()
        判断是是否目录
        
    os.path.join()
        将多个路径组合返回一个路径
        样例： os.path.join("test1", "test2")
    
    os.path.getsize()
        返回文件内容字符串的长度
        样例： os.path.getsize("test.txt") ,返回的是文件test.txt的内容的字符串长度
        
    os.walk()
        可以对目录进行递归，返回的时候一个三元组(父目录，子目录，文件)
        方法walk(top, topdown=True, onerror=None, followlinks=False)：
            topdown=True：默认遍历递归从上到下.
            onerror=None：默认不调用任何函数.
            followlinks=False：默认不遍历超连接；
        返回的结果中：
            父目录是字符串
            子目录是list
            文件是list

    
"""


def os_oper():
    # 操作系统名称
    # print(os.name)
    # 环境变量获取
    # print(os.environ)
    # print(os.getenv("CLASSPATH"))
    # print(os.environ.get("CLASSPATH"))
    # print(os.getenv("aa", "未找到环境变量"))
    # print(os.environ.get("aa", "未找到环境变量"))
    # 获取当前操作系统的系统路径分隔符
    # print(os.sep)
    # 获取当前操作系统的行分隔符
    # print("'"+os.linesep+"'")

    # 文件及文件夹操作
    # print(os.getcwd())
    # os.chdir("E:\\07-python\\07-projectList\\a01PythonLearn\\file")
    # print(os.getcwd())
    # os.makedirs("E:\\07-python\\07-projectList\\a01PythonLearn\\file" + "\\file01\\file02")
    # os.mkdir("E:\\07-python\\07-projectList\\a01PythonLearn\\file" + "\\file03")
    # print(os.listdir())
    # os.rename("file03", "file04")
    # print(os.listdir())
    # os.removedirs("E:\\07-python\\07-projectList\\a01PythonLearn\\file" + "\\file01\\file02")
    # os.rmdir("E:\\07-python\\07-projectList\\a01PythonLearn\\file" + "\\file04")
    # print(os.listdir())
    # print(os.stat("file03.txt"))

    # 路径操作
    cwd = os.getcwd()
    print(cwd)
    print(os.path.abspath(cwd))

    return


def view_file_path(file_path):
    """
    遍历目录下的所有子目录及文件
    :param file_path:
    :return:
    """
    # path = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    try:
        for root, dirs, files in os.walk(file_path):
            print('-' * 50 + "根目录" + '-' * 50)
            print(root)
            print('-' * 50 + "目录" + '-' * 50)
            print(dirs)
            print('-' * 50 + "文件" + '-' * 50)
            print(files)
    except Exception as e:
        print(e)


def zip_file_path(src_file_path, zip_file_path):
    """
    压缩文件夹到指定路径&指定名称
    :param src_file_path: 来源文件目录
    :param zip_file_path: 目录文件路径
    :return:
    """
    result = True
    # pathwalk = r"E:\\07-python\\07-projectList\\a01PythonLearn\\walk"
    # pathfile = r"E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    LogTime = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))

    if not os.path.exists(zip_file_path):
        os.path.makedirs(zip_file_path)
    os.chdir(zip_file_path)
    print(os.getcwd())
    try:
        with zipfile.ZipFile(LogTime + ".zip", 'w') as zip:
            zip_list = []
            for root, dirs, files in os.walk(src_file_path):
                for file in files:
                    zip_list.append(os.path.join(root, file))
                for dir in dirs:
                    zip_list.append(os.path.join(root, dir))
            for i in zip_list:
                zip.write(i, i.replace(src_file_path, ''))
    except Exception as e:
        print(e)
        result = False

    return result


if __name__ == "__main__":
    # os_oper()
    zip_file_path = r"E:\\07-python\\07-projectList\\a01PythonLearn\\walk"
    src_file_path = r"E:\\07-python\\07-projectList\\a01PythonLearn\\file\\"
    # print(zip_file_path(src_file_path, zip_file_path))

    print(os.path.split(src_file_path))
    print(os.path.basename(src_file_path))
    print(os.path.dirname(src_file_path))
    print(os.path.isfile(os.path.split(src_file_path)[1]))
    print(os.path.isdir(os.path.split(src_file_path)[0]))
    print(os.path.join(src_file_path, zip_file_path))
    print(os.path.getsize(src_file_path + "file01.txt"))

    view_file_path(src_file_path)
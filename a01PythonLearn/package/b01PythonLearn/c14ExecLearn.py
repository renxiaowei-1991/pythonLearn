#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import file

"""
异常exception
    异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
    异常是Python对象，表示一个错误。
    当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行

    Python提供了两个非常重要的功能来处理python程序运行中出现的异常和错误。可以使用该功能来调试python程序。
        异常处理
        断言

异常处理
    捕捉异常可以使用 try/except 语句。
    try/except 语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
    如果你不想在异常发生时结束你的程序，只需在try里捕获它
    语法：
        try:
            <语句>    #运行别的代码
        except <名字>:
            <语句>    #如果在try部分引发了'name'异常
        except <名字>,<数据>:
            <语句>    #如果引发了'name'异常，获得附加的数据
        else：
            <语句>    #如果没有发生异常

    try工作原理
        当开始一个try语句后，python就在当前程序的上下文中做标记，这样当异常出现时就可以回到这里，
        try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
        1、如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句(除非在处理异常时又引发新的异常)
        2、如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层(这样将结束程序，并打印默认的出错信息)
        3、如果在try子句执行时没有发生异常，python将执行else语句后的语句(如果有else的话)，然后控制流通过整个try语句

    except可以不带任何异常类型
        try:
            正常的操作
            ......
        except:
            发生异常，执行这块代码
            ......
        else:
            如果没有异常执行这块代码

    以上方式try-except语句捕获所有发生的异常。但这不是一个很好的方式，不能通过该程序识别出具体的异常信息。

    except可以带多种异常类型
        try:
            正常的操作
            ......
        except (Exception1[,Exception2[,ExceptionN]]):
            发生以上多个异常中的一个，执行这块代码
            ......
        else:
            如果没有异常执行这块代码

    try-finally语句
        try-finally语句无论是否发生异常都将执行最后的代码。
        try:
            <语句>
        finally:
            <语句>    #退出try时总会执行
        raise

    try-except-else 可以进行嵌套

触发异常|raise
    可以使用raise语句自己触发异常
    raise语法格式如下：
        raise [Exception [, args [, traceback]]]

    语句中Exception是异常的类型(例如：NameError)参数标准异常中任一种。
    args是自己提供的异常参数。
    trackback是可选的(实践中很少使用)，如果存在，是跟踪异常对象。

    raise三种常用用法
    1、raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常
    2、raise 异常类名称：raise 后带一个异常类名称，表示引发执行类型的异常
    3、raise 异常类名称(描述信息)：在引发指定类型的异常的同时，附带异常的描述信息。

    样例：
        try:
            print("raise练习")
            raise(Exception,"通过raise抛出异常")
        except Exception as err:
            print("1",err)
        else:
            print("2")

        try:
            print("raise练习")
            raise(ValueError,"通过raise抛出异常")
        except ValueError as err:
            print("1",err)
        else:
            print("2")

        说明：
            Exception as err
            ValueError as err
                标识为捕捉到的异常重命名

            raise(Exception,"通过raise抛出异常")
            raise(ValueError,"通过raise抛出异常")
                引号中的内容标识，手动抛出异常的时候顺带输出的信息

自定义异常
    通过创建一个新的异常类，程序可以命名它们自己的异常。
    异常应该是典型的集成自Exception类，通过直接或者间接的方式。


标准异常
    BaseException      所有异常的基类
    SystemExit         解释器请求退出
    KeyboardInterrupt  用户中断执行(通常是输入^C)
    Exception          常规错误的基类
    StopIteration      迭代器没有更多的值
    GeneratorExit      生成器(generator)发生异常来通知退出
    StandarError       所以的内建标准异常的基类
    ArithmeticError    所以数值计算错误的基类
    FloatingPointError 浮点计算错误
    OverflowError      数值运算超出最大限制
    ZeroDivsionError   除(或取模)零(所以数据类型)
    AssertionError     断言语句失败
    AttributeError     对象没有这个属性
    EOFError           没有内建输入，到达EOF标记
    EnvironmentError   操作系统错误的基类
    IOError            输入/输出操作失败
    OSError            系统调用失败
    WindowsError       系统调用失败
    ImportError        导入模块/对象失败
    LookupError        无效数据查询的基类
    IndexError         序列中没有此索引(index)
    KeyError           映射中没有这个键
    MemoryError        内存溢出错误(对于Python解释器不是致命的)
    NameError          未声明/初始化对象(没有属性)
    UnboundLocalError  访问未初始化的本地变量
    RuntimeError       一般的运行时错误
    NotImplementedError 尚未实现的方法
    SyntaxError         Python语法错误
    IndentationError    缩进错误
    TabError            Tab和空格混用
    SystemError         一般的解释器系统错误
    TypeError           对类型无需的操作
    ValueError          传入无效的参数
    UnicodeError        Unicode相关的错误
    Warning             警告的基类


"""


def exceptLearn():
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn"
    try:
        # 文件路径
        subFilePath = "\\file\\a01PythonLearnFile\\"
        fileName = "b02ExceLearnFile.txt"
        # 打开文件
        file01 = open(rootPath + subFilePath + fileName, "w+", encoding="utf-8")
        file01.write("这是一个测试文件，用于测试异常!!")

    except IOError:
        print("Error：没有找到文件或读取文件失败")
    else:
        print("内容写入文件成功")
        # 关闭文件
        print("当前文件:", file01.name, ",文件打开方式:", file01.mode, ",文件关闭状态:", file01.closed)
        if file01.closed == False:
            file01.close()
        print("当前文件:", file01.name, ",文件关闭状态:", file01.closed)


def tryFinallyLearn():
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn"
    try:
        # 文件路径
        subFilePath = "\\file\\a01PythonLearnFile\\"
        fileName = "b02ExceLearnFile.txt"
        # 打开文件
        file01 = open(rootPath + subFilePath + fileName, "w+", encoding="utf-8")
        file01.write("这是一个测试文件，用于测试异常!!")

    finally:
        print("内容写入文件成功")
        # 关闭文件
        print("当前文件:", file01.name, ",文件打开方式:", file01.mode, ",文件关闭状态:", file01.closed)
        if file01.closed == False:
            file01.close()
        print("当前文件:", file01.name, ",文件关闭状态:", file01.closed)


def raiseExceptionLearn():
    try:
        print("raise练习")
        raise (Exception, "通过raise抛出异常")
    except Exception as err:
        print("1", err)
    else:
        print("2")


# 自定义异常
class customeError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


def customeErrorTest():
    try:
        # 手动抛出自定义异常customeError 标识RuntimeError类型的参数
        raise customeError("手动抛出自定义异常customeError")
    except customeError as cusE:
        print("捕捉手动抛出的异常customeError")
    else:
        print("成功执行")
    return


def exception_test_func():
    """
    测试写文件，文件异常
    :return:
    """
    base_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\"
    file_name = "file05.txt"
    log_base_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\log\\"
    log_file_name = "log01.log"
    try:
        log01 = open(log_base_path + log_file_name, 'w+', encoding='utf-8')
        file01 = open(base_path + file_name, 'w+', encoding='utf-8')
        file01.write("这是一个测试文件，用来测试except！\n")
        raise IOError("手动触发IOError! \n")
    except IOError:
        print("文件写入IO异常！")
        log01.write("文件写入IO异常！\n")
    except ValueError:
        print("文件写入Value异常！")
        log01.write("文件写入Value异常！\n")
    else:
        print("文件写入成功！")
        log01.write("文件写入成功！\n")
    finally:
        if not file01.closed:
            file01.close()
        print("文件已关闭！")
        log01.write("文件已关闭！\n")
        if not log01.closed:
            log01.close()
    return


if __name__ == '__main__':
    print(__file__)
    # exceptLearn()
    # tryFinallyLearn()
    # raiseExceptionLearn()
    customeErrorTest()
    
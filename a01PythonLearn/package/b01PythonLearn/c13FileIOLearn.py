#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import file

"""
文件I/O
    File对象 和 OS对象提供了很多文件与目录的操作方法
    File 对象方法
        file对象提供了操作文件的一系列方法
    OS 对象方法
        提供了处理文件及目录的一系列方法

打印到屏幕
    print()

读取键盘输入
    python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。
    raw_input([prompt])
        从标准输入读取一行，并返回一个字符串(去掉结尾的换行符)
        prompt 是用来进行输入提示的内容
        python3.0已弃用
    input([prompt])
        和 raw_input 基本类似。但是input可以接收一个python表达式作为输入，并将运算结果返回。
        input希望读取一个合法的python表达式，输入字符串的时候必须用引号括起来，否则会引发SyntaxError
        除非对input()有特别需要，否则一般建议使用raw_input()来进行交互

    注意：
        1、python2.x中，raw_input() 和 input() 都存在
        2、python3.x中，raw_input() 和 input() 进行了整合，只保留了input()
            可以接收任意性输入，将所有输入默认为字符串进行处理，并返回字符串类型

打开&关闭&读写文件
    python提供了必要的函数和方法进行默认情况下的文件基本操作。可以用file对象做大部分的文件操作

    open()
        打开一个文件，创建一个file对象
        必须先用open()打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
        语法：
            object = open(file_name[, access_mode][, buffering])
        完整格式：
            object = open(fileName, mode='r', buffering=-1, encoding=None, errors=None, newLine=None, closefd=True, opener=None)

            说明：
                file_name：一个包含了要访问的文件名称的字符串值
                access_mode：决定了打开文件的模式：只读，写入，追加等。默认文件访问模式为只读(r)，这个参数是非强制性的。
                    t   文本模式(默认)
                    x   写模式，新建一个文件，如果该文件已存在则会报错
                    b   二进制模式
                    +   打开一个文件进行更新(可写可读)
                    U   通用换行模式(不推荐)

                    r   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
                    rb  以二进制格式打开一个文件用于只读。文件指针将会放在文件开头。这是默认模式。一般用于非文本文件，如图片等。
                    r+  打开一个文件用于读写。文件指针将会放在文件的开头。
                    rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件，如图片等。
                    w   打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
                    wb  以二进制格式打开一个文件只用于写入。如果该文件已经存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件，如图片等。
                    w+  打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
                    a   打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
                    ab  以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。一般用于非文本文件，如图片等。
                    a+  打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结果。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
                    ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结果。如果该文件不存在，创建新文件用于读写。

                    总结：
                        r  只读(从头开始)(不覆盖文件)(不可以创建新文件)(不覆盖文件)
                        w  只写(清除原内容)(从头开始)(可以创建新文件)(覆盖文件)
                        a  只写(不清除原内容)(从尾开始)(可以创建新文件)(不覆盖文件)

                        r+ 读写(不清除原内容)(从头开始)(不可以创建新文件)(不覆盖文件)
                        w+ 读写(清除原内容)(从头开始)(可以创建新文件)(覆盖文件)
                        a+ 读写(不清除原内容)(从尾开始)(可以创建新文件)(不覆盖文件)

                    注意：
                        w+  以w+模式打开文件的时候，文件里面的内容就会被删除。所以如果只是要读取，不能用w+模式，要用r+

                buffering：
                    设置缓存
                    如果buffering的值被设置为0，就不会有寄存。
                    如果buffering的值被设置为1，访问文件时会寄存。
                    如果buffering的值被设置为大于1的整数，表明了这就是寄存区的缓存大小。
                    如果buffering的值被设置为负值，寄存区的缓存大小则为系统默认。

                encoding  文件编码格式。一般使用utf8
                errors    报错级别
                newline   区分换行符
                closefd   传入的file参数类型
                opener    设置自定义开启器，开启器的返回值必须是一个打开的文件描述符

        file对象的属性
            一个文件被打开后，就有了一个file对象，可以得到有关该文件的各种属性。
            file对象属性列表如下：
                file.closed    file文件开关状态。true：文件已被关闭；false：文件未被关闭。
                file.mode      返回被打开文件的访问模式。
                file.name      返回文件的名称
                file.softspace 如果用print输出后，必须跟一个空格符，则返回false。否则返回true
                    python3.x 中softspace已经被移除

    close()
        close()方法刷新缓存区里任何还没写入的信息，并关闭该文件，之后便不能再进行写入。
        当一个文件对象的引用被重新指定给另一个文件时，python会关闭之前的文件。
        用close()方法关闭文件是一个很好的习惯。
        语法：
            fileObject.close()

    write()
        write()方法可将任何字符串写入一个打开的文件。
        python字符串可以是二进制数据，而不是仅仅是文字。
        write()方法不会在字符串的结果添加换行符('\n')
        语法：
            fileObject.write(String)
            被传递的参数是要写入到已打开的文件的内容。

    read([count])
        read()方法从一个打开的文件中读取一个字符串。
        python字符串可以是二进制数据，而不仅仅是文字。
        语法：
            fileObject.read([count])
            被传递的参数是要从已打开文件中读取的字节计数。
            该方法从文件的开头开始读入，如果没有传入count，会尝试尽可能多地读取更多的内容，很可能是直接到文件的末尾。

        注意：
            打开一个文件，先写后读，先读后写，会有冲突，指针的位置问题。
            先写后读：写完之后，指针在最后，这时候直接读，读到的内容是空。

    flush()
        刷新文件内部缓存，直接把内部缓存数据立刻写入文件，而不是被动等待输出缓存区写入

    next()
        返回文件下一行
        报错： AttributeError: '_io.TextIOWrapper' object has no attribute 'next'
        原因：
            next()的实现方式已变更。原来的语法是，fileObject.next() ，现在的语法如下：
                next(fileObject,default)
                其中：
                    fileObject:读取的文件
                    default:读取完成后剩余循环次数返回的默认值。
                        如果不写default值，会返回异常：StopIteration

    readline([size])
        读取整行，包括"\n"字符
    readlines([sizeint])
        读取所以行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力
    truncate()
        截取文件，截取的字节数通过size字段，默认为当前文件位置
    writelines(sequence)
        向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符

文件定位        
    tell()
        tell()方法返回文件内的当前位置(指针位置)
        也就是说，下一次的读写会发生在文件开头的这么多字节之后。

    seek(offset[, from])
        改变当前文件的位置。
        offset变量标识要移动的字节数。
            报错 io.UnsupportedOperation: can't do nonzero cur-relative seeks
            原因：
                python的文件打开中，没有使用b模式选项打开文件，只允许从文件头开始计算相对位置
                访问模式改为rb或rb+即可

        from
            变量指定开始移动字节的参考位置。
            from被设置为0，表示将文件的开头作为移动字节的参考位置。
            from被设置为1，表示将当前的位置作为参考位置。
            from被设置为2，表示将文件的末尾作为参考位置。

重命名&删除文件
    os模块提供了执行文件处理操作的方法，例如重命名&删除文件

    rename()
        rename()方法需要两个参数，当前的文件名和新文件名
        语法：
            os.rename(currentFileName, newFileName)

    remove()
        remove()方法可以删除文件，参数是要删除的文件名
        语法：
            os.remove(fileName)

目录操作
    所有文件都包含在各个不同的目录下，python都可以处理。
    os模块提供了很多方法能进行 创建、删除、更改目录的操作。

    mkdir()
        在当前目录下创建新的目录
        语法：
            os.mkdir(newDir)

    chdir()
        改变当前的目录。参数是想要设置成当前目录的目录名称
        语法：
            os.chdir(newDir)

    getcwd()
        获取当前的工作目录

    rmdir()
        删除目录，参数是目录名称
        在删除目录之前，它的所有内容应该先被删除。
        语法：
            os.rmdir(fileDir)

        注意：
            如果已经使用chdir()改变到了改目录，删除的时候会报错。
            需要先变更工作目录。在删除目录

    os.chmod(path,mode)
        更改权限.该方法没有返回值
        path  文件名路径或者目录路径
        flags 
            -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用
            stat.S_IXOTH: 其他用户有执行权0o001
            stat.S_IWOTH: 其他用户有写权限0o002
            stat.S_IROTH: 其他用户有读权限0o004
            stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
            stat.S_IXGRP: 组用户有执行权限0o010
            stat.S_IWGRP: 组用户有写权限0o020
            stat.S_IRGRP: 组用户有读权限0o040
            stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
            stat.S_IXUSR: 拥有者具有执行权限0o100
            stat.S_IWUSR: 拥有者具有写权限0o200
            stat.S_IRUSR: 拥有者具有读权限0o400
            stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
            stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
            stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
            stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
            stat.S_IREAD: windows下设为只读
            stat.S_IWRITE: windows下取消只读

        样例：
            os.chmod("/tmp/foo.txt", stat.S_IXGRP)
            os.chmod("/tmp/foo.txt", stat.S_IWOTH)

    os.chown(path, uid, gid)
        更改文件所有者

文件操作
    os模块的文件操作

    os.path
        模块主要用于获取文件的属性，方法非常多。个别如下：


        os.path.abspath(path)  返回绝对路径
        os.path.basename(path) 返回文件名
        os.path.dirname(path)  返回文件路径
        os.path.exists(path)   判断路径path是否存在
        os.path.isfile(path)   判断路径是否为文件
        os.path.isdir(path)    判断路径是否为目录


"""


# 从标准输入获取内容
def getInput(info):
    str1 = input(info)
    print("你输入的内容是：", str1)
    return str1


# 文件操作
# 写文件
def writeFileOperFunc():
    # 指定根目录
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    # 打开文件
    file01 = open(rootPath + "\\a01PythonLearnFile\\b01FileIOLearnFile.txt", "w+")

    # 写文件
    print("当前指针位置：", file01.tell())
    file01.write("www.runoob.com!\nVery good site!\n")
    print("当前指针位置：", file01.tell())

    # 关闭文件
    print("文件 ", file01.name, "，访问模式：", file01.mode, "，关闭状态是：", file01.closed)
    if file01.closed == False:
        file01.close()
    print("文件 ", file01.name, "，关闭状态是：", file01.closed)


# 读文件
def readFileOperFunc():
    # 指定根目录
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    # 打开文件:不能用w+，打开文件的时候，文件内的内容就会被清空，需要用r+
    file01 = open(rootPath + "\\a01PythonLearnFile\\b01FileIOLearnFile.txt", "rb+")

    # 读文件
    print("当前指针位置：", file01.tell())
    str01 = file01.read(10)
    print("从文件中读取的内容是：\n", str01)
    print("从文件中读取的内容长度是：", len(str01))
    print("当前指针位置：", file01.tell())
    # 移动指针
    file01.seek(10, 1)
    print("指针移动后，当前指针位置：", file01.tell())
    str02 = file01.read(10)
    print("从文件中读取的内容是：\n", str02)
    print("从文件中读取的内容长度是：", len(str02))
    print("当前指针位置：", file01.tell())

    # 关闭文件
    print("文件 ", file01.name, "，访问模式：", file01.mode, "，关闭状态是：", file01.closed)
    if file01.closed == False:
        file01.close()
    print("文件 ", file01.name, "，关闭状态是：", file01.closed)


# 循环读取文件readLines
def readLinesFileOperFunc():
    # 指定根目录
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    # 打开文件:不能用w+，打开文件的时候，文件内的内容就会被清空，需要用r+
    file01 = open(rootPath + "\\a01PythonLearnFile\\b01FileIOLearnFile.txt", "r+")

    # 读取文件
    # for line in file01.readlines():
    #     print(line)
    fileContent = [line for line in file01.readlines()]
    print("被读取文件：", file01.name, "，文件内容是：\n", fileContent)

    # 关闭文件
    print("文件 ", file01.name, "，访问模式：", file01.mode, "，关闭状态是：", file01.closed)
    if file01.closed == False:
        file01.close()
    print("文件 ", file01.name, "，关闭状态是：", file01.closed)


# 循环读取文件next
def nextFileOperFunc():
    # 指定根目录
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    # 打开文件:不能用w+，打开文件的时候，文件内的内容就会被清空，需要用r+
    file01 = open(rootPath + "\\a01PythonLearnFile\\b01FileIOLearnFile.txt", "r+")

    # 读取文件
    # for line in range(5):
    #     print(next(file01,'1'))
    # fileContent = [file01.next() for i in range(5)]
    fileContent = [next(file01, '1') for i in range(5)]
    print("被读取文件：", file01.name, "，文件内容是：\n", fileContent)

    # 关闭文件
    print("文件 ", file01.name, "，访问模式：", file01.mode, "，关闭状态是：", file01.closed)
    if file01.closed == False:
        file01.close()
    print("文件 ", file01.name, "，关闭状态是：", file01.closed)


# 文件变更
def renameFileOperFunc():
    # 指定根目录
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    currFileName = "\\a01PythonLearnFile\\b01FileIOLearnFile.txt"
    newFileName = "\\a01PythonLearnFile\\b01FileIOLearnFile01.txt"
    os.rename(rootPath + currFileName, rootPath + newFileName)


# 文件删除
def removeFileOperFunc():
    # 指定根目录
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    fileName = "\\a01PythonLearnFile\\b01FileIOLearnFile01.txt"
    os.remove(rootPath + fileName)


# 目录操作
def dirFileOperFunc():
    # 指定根目录
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    # 指定子目录
    subFilePath = "\\a01PythonLearnFile"
    # 目录操作
    newFiledir = "\\b01FileIOLearnFileSubPath"
    newFilePath = rootPath + subFilePath + newFiledir
    # print("当前工作路径：",os.getcwd())
    # os.mkdir(newFilePath)
    projectPath = os.getcwd()
    print("当前工作路径：", os.getcwd())
    os.chdir(newFilePath)
    print("当前工作路径：", os.getcwd())
    os.chdir(projectPath)
    print("当前工作路径：", os.getcwd())
    os.rmdir(newFilePath)


def get_input_file(filepath, filename):
    """
    从标准输入读取内容，存入文件中
    :param filepath:文件存储路径
    :param filename:文件名
    :return:
    """
    # 打开文件，进行读写，如果不存在，创建新文件
    file01 = open(filepath + filename, 'w+')
    # 从标准输入循环读取内容，知道输入的是，结束输入
    print("当前指针位置：", file01.tell())
    in_str = input("请输入内容：")
    while in_str != "end":
        file01.write(in_str + "\n")
        in_str = input()
    # 将缓存区文件写入文件
    file01.flush()
    print("当前指针位置：", file01.tell())
    print("当前操作文件：", file01.name, ",打开模式是：", file01.mode, "，关闭状态是：", file01.closed)
    # 关闭文件
    if not file01.closed:
        file01.close()
    print("当前操作文件：", file01.name, ",打开模式是：", file01.mode, "，关闭状态是：", file01.closed)
    return


def get_file_details(filepath, filename):
    """
    读取指定文件内容
    :param filepath:文件存储路径
    :param filename:文件名
    :return:
    """
    file01 = open(filepath + filename, 'r+')
    print("文件：", filepath + filename, "的内容是：\n")
    for line in file01.readlines():
        print(line, end="")
    if not file01.closed:
        file01.close()
    return


def copy_file_func(srcfile01, srcfile02):
    """
    复制文件，将文件filename01的内容复制到filename02中。
    如果filename01不存在，返回提示结果。
    :param srcfile01:
    :param srcfile02:
    :return:
    """
    if os.path.exists(srcfile01):
        file01 = open(srcfile01, 'r+')
        file02 = open(srcfile02, 'w+')
        for line in file01.readlines():
            file02.write(line)
        if not file01.closed:
            file01.close()
        if not file02.closed:
            file02.close()
    else:
        print("文件：", srcfile01, " 不存在！")
    return


def file_merge_func(srcfile01, srcfile02, tarfile):
    """
    合并文件srcfile01和srcfile02，将结果存入tarfile
    :param srcfile01: 来源文件01
    :param srcfile02: 来源文件02
    :param tarfile: 目标文件
    :return:
    """
    if os.path.exists(srcfile01) and os.path.exists(srcfile02):
        file01 = open(srcfile01, 'r+')
        file02 = open(srcfile02, 'r+')
        file03 = open(tarfile, 'w+')
        for line in file01.readlines():
            file03.write(line)
        for line in file02.readlines():
            file03.write(line)
    elif not os.path.exists(srcfile01):
        print("文件：", srcfile01, " 不存在！")
    else:
        print("文件：", srcfile02, " 不存在！")
    if not file01.closed:
        file01.close()
    if not file02.closed:
        file02.close()
    if not file03.closed:
        file03.close()
    return


def rename_file_func(oldfilename, newfilename):
    """
    修改文件名
    :param oldfilename:
    :param newfilename:
    :return:
    """
    if os.path.exists(oldfilename):
        os.rename(oldfilename, newfilename)
    return


def remove_file_func(filename):
    if os.path.exists(filename):
        os.remove(filename)
    return


def path_change_func(basepath):
    """
    目录创建和目录变更的练习
    :param basepath:
    :return:
    """
    if not os.path.exists(basepath + "\\a01filetest"):
        os.mkdir(basepath + "\\a01filetest")
    print(os.getcwd())
    os.chdir(basepath + "\\a01filetest")
    print(os.getcwd())
    return


if __name__ == '__main__':
    # print(getInput("请输入："))
    print(__file__)
    # 写文件
    # writeFileOperFunc()
    # 读文件
    # readFileOperFunc()
    # 文件变更
    # renameFileOperFunc()
    # 文件删除
    # removeFileOperFunc()
    # 目录操作
    # dirFileOperFunc()
    # 循环读取文件readLines
    # readLinesFileOperFunc()
    # 循环读取文件next
    nextFileOperFunc()

    # 文件存储根目录
    base_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\"
    # get_input_file(base_path, "inputFile.txt")
    # get_file_details(base_path, "inputFile.txt")
    # copy_file_func(base_path + "file02.txt", base_path + "file03.txt")
    # file_merge_func(base_path + "file02.txt", base_path + "file03.txt", base_path + "file04.txt")
    # rename_file_func(base_path + "file04.txt", base_path + "file05.txt")
    # copy_file_func(base_path + "file05.txt", base_path + "file04.txt")
    # remove_file_func(base_path + "file05.txt")
    path_change_func(base_path)
    
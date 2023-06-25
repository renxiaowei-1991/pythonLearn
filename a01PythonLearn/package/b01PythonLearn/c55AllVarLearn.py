#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

"""
    __name__
        指向模块的名字
        主模块被调用的时候，__name__ == '__main__'
        相对导入使用模块的__name__属性来确定该模块在包层次结构中的位置。
        如果模块的名称不包含任何包信息(例如'__name__')，则相对导入将被视为该模块是顶级模块来进行解析，而不管模块实际位于文件系统上的什么位置
        启动模块被调用的时候，__name__ == '__main__'，这个__name__不包含启动模块所在包的任何信息，所以启动模块会被当成顶级模块来进行解析，而不管模块实际位于文件系统什么位置
        非启动模块被调用的时候，__name__ == package1.package2.package3.module4。可以在被调用的各模块中输出__name__来查看
            例如：a02ProjectTest01.package1.module2

    __package__
        提议的主要更改是引入了新的模块级别属性__package__。如果存在，则相对导入将基于此属性而非模块__name__属性
        __package__应该设置模块的属性。它的值必须是字符串，但可以与其值相同__name__。如果该属性设置为None或丢失，则导入系统将使用更合适的值填充该属性。
        当模块是软件包时，其__package__值应设置为__name__。如果模块不是软件包，__package__则对于顶级模块或子模块，应将其设置为空字符串，并将其设置为父软件包的名称
        包的层次名

    __file__
        指向该模块的导入文件名
        可以通过文件名获取文件所在目录
        可以通过获取到的目录，用来修改 sys.path
        sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
        os.path.dirname(__file__)
        	表示文件(文件夹)所在路径
         os.path.dirname(os.path.dirname(__file__))
         	表示文件夹所在路径
    sys.path
        是一个列表 list ,它里面包含了已经添加到系统的环境变量路径。
        当我们要添加自己的引用模块搜索目录时，可以通过列表 list 的 append()方法；
        sys.path.append()
        对于需要引用的模块和需要执行的脚本文件不在同一个目录时，可以按照如下形式来添加路径：
        例如：
        1) 导入的XX包在另一个项目文件中，在自己写的程序中需要用到XX包。
        2) 所以我们在运行自己写的程序时，首先加载导入的XX包，加载的时候python解释器会去sys.path默认搜索路径去搜索。
        3) 如果通过sys.path中的路径可以搜索到XX包，然后加载。
        4) 如果无法通过sys.path中的路径搜索到XX包，即说明自己的程序中引用的XX包，与自己程序脚本所在目录不在同一个路径。（无法在自己的程序脚本中根据默认搜索路径查找到XX包）
        5) 然后我们就需要将XX包的搜索路径添加到自己程序脚本的默认搜索路径中，重新运行自己的程序脚本，先搜索XX包在家载XX包。
"""

print("程序名：", __name__)
print("包名：", __package__)
print("文件名：", __file__)
print("文件绝对路径(包含文件名)：", os.path.abspath(__file__))
print("文件绝对路径(不包含文件名，如果参数是文件夹，则获取该文件夹所在文件夹路径)：", os.path.dirname(__file__))
print(sys.path)
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
print(sys.path)

from moduleTest02 import bar01

print(__name__, __package__)

# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


#!/use/bin/env python
# -*- coding:utf-8 -8-

import sys
import os

# 相对导入：如果作为 主程序 __main__ 执行，不能使用相对引用，会报错
# 包含__main__的模块，可以放在任何层级目录中。所以主程序所在模块不能使用相对引用，只能使用绝对引用
# from . import b53ModLearn

# from ..a02PkgImpTest.b02PythonLearnPkg.c02ModuleTest02 import function07

# 绝对导入
# from imp import reload #python3.4之前
from importlib import reload

from package.a01PythonLearn import b53ModLearn
from package.a02PkgImpTest.b02PythonLearnPkg.c02ModuleTest02 import function07
from package.a02PkgImpTest.b02PythonLearnPkg import c03PackageTest01

"""
基本概念
    模块  一个Python模块实际上就是一个文件，它的文件格式为.py
    包    一个Python包就是一个文件夹folder，里面含有模块文件(这=个文件夹要有一个空的__init__.py文件，也可以不空)

    模块可以是函数function、类class、一段代码...

import原理
    假如导入了一个模块：
        import bao
    1、python首先在sys.modules中查找bao这个名称。它是先前曾被导入过的所有模块的缓存(就是之前被导入过的模块，都被暂时保存在里面)
    2、如果在这个缓存中找不到这个名称，python接下来会去内置的模块built-in modules中查找(这些内置模块是python预装的，可以在python标准库中查看详情)
    3、如果还是没在内置模块中找到它，python将会去sys.path定义的文件夹列表中搜索(通常来说，这个列表会包括当前目录，并且会先在里面搜索)
    4、当python找到了模块，它会将这个模块绑定到局部作用域。这就表示当前这个bao已经被定义了并且在被当前文件使用而不会抛NameError的异常
    5、如果这个模块名没有被找到，就会抛出ModuleNotFoundError这个异常

导入方式
    可以从一个包或者模块中导入指定的对象，一般导入方法有以下两种：
    1、 import bao
    2、 from bao import yang 

    第一种方式，可以直接导入该资源，bao可以是一个包或者模块
    第二种方式，从其他包或者模块导入资源，yang可以是一个模块、子包subpackage、对象object，例如：类class，或者函数function

PEP8规范
    1、导入应该总是写在最前面，但需尾随任何模块单行注释和文档注释
    2、导入应该根据导入的内容进行分类，一般有三种：
        导入标准库(Python的内置模块)
        导入相关的第三方包(不属于当前引用的第三方包)
        导入本地引用的模块(属于当前引用的模块)

        每一组的导入都应该用空白行分割

绝对引用
    绝对导入通过使用被导入资源在项目根目录的完整路径进行导入

    语法：
        假如有如下目录结构：
            project
                package1
                    module1.py
                    module2.py
                        function1|函数
                package2
                    __init__.py
                        class1|类
                    module3.py
                    module4.py
                    subpackage1
                        module5.py
                            function2|函数

        这里有个目录project，包含两个子目录：package1、package2。
        其中package1有两个文件：module1.py、module2.py。
        package2有三个文件：两个模块，module3.py、module4.py，以及一个初始化文件 __init__.py。
        也包括一个目录，subpackage，它包含一个文件，module5.py。

        假设存在以下内容： 
            package1/module2.py有一个函数，叫function1
            package2/__init.py有一个类，叫class1
            package2/subpackage1/module5.py有一个函数，叫function2

        绝对导入样例：
            from package1 import module1
            from package1.module2 import function1
            from package2 import class1
            from package2.subpackage1.module5 import function2

    注意：
        必须在顶级包目录top-level package下提供每个包或者文件具体的路径。某种程度上和其文件路径相识，但是会使用点dot(.)，而不是使用斜线slash(/)

    优缺点
        绝对引用简单明了。使用后，仅通过导入语句，就知道资源是从哪里导入的。而且，即使当前位置的导入语句改变了，绝对导入还是会保持有效。应该优先考虑使用绝对引用，并且PEP8 推荐使用绝对引用

相对引用
    取决于目录结构的复杂程度，有时绝对路径会变得冗长。如下：
        from package1.subpackage2.subpackage3.subpackage4.module5 import function6
    这种导入相对繁杂，此时相对引用在这种情况下是一个绝佳的选择！
    **相对引用指定了被导入资源是相对于当前的位置，即，这个位置就是导入语句所在的地方。

    实例
        相对引用的语法取决于当前的位置和被导入模块、包、对象 的位置。例如：
            from .some_module import some_class
            from ..some_package import some_function
            from . import some_class
        能看到至少有一个点在每一个导入语句的前面。相对引用利用点符号来指定位置。
            1、单个点表示模块或者包的引用是在同一个位置的同一个目录下
            2、两个点表示它是在当前位置的父目录中，即，上一级目录
            3、三个点表示位于祖父母目录中，以此类推。与类Unix系统 cd ..等命名了相识

        假如有如下目录结构：
            project
                package1
                    module1.py
                    module2.py
                        function1|函数
                package2
                    __init__.py
                        class1|类
                    module3.py
                    module4.py
                    subpackage1
                        module5.py
                            function2|函数

            #package1/module1.py
            from .module2 import function1

            这里只需要使用一个点，因为module2.py和当前的模块module1.py在同一个路径下面。
            也可以在package2/module3.py中导入class1和function2通过以下方法：

            #package2/module3.py
            from . import class1
            from .subpackage1.module5 import function2

            在第一个导入语句中，单个点代表你从当前包中导入class1。
            注意：
                导入一个包实际上是导入包里面的__init__.py文件作为模块
            第二个导入语句中，再次使用了单个点，这是因为subpackage1和当前模块module3.py是同一个目录

    优缺点
        相对引用非常简洁。取决于当前的位置，可以将冗长语句缩减到一下：
            from ..subpackage4.module5 import function6

        相对引用可能引起混乱，特别是一些目录结构可能会改变的共享项目。且相对引用不想绝对引用那样可读，
        不能轻易的从导入语句查看资源被导入的位置

结论
    一般情况下，应该选择绝对导入而不是使用相对导入，除非路径非常复杂
"""

"""    
模块
    python模块(Module)，是一个Python文件，以.py结尾，包含了python对象定义和python语句
    模块能够有逻辑地组织python代码段
    把相关的代码分配到一个模块里能让代码更好用，更易懂
    模块能定义函数，类，变量，模块里也能包含可执行的代码

import语句(模块的引入)
    模块定义好后，可以使用import语句来引入模块
    import module1[, module2[,... moduleN]]
    例如：
        import math

    模块中函数的调用
        模块名.函数名
        例如：
            math.abs()

    当解释器遇到import语句，如果模块在当前的搜索路径就会被导入。
    搜索路径是一个解释器会先进行搜索的所有目录的列表。如果想要导入模块，需要把命令放在脚本最前端

from...import语句
    from语句从模块中导入一个指定的部分到当前命名空间
    from modname import name1[, name2[, ...nameN]]
    例如：
        from fib import fibonacci

    from...import* 等价于 import ...

搜索路径
    当导入一个模块，python解析器对模块位置的搜索顺序是：
        1、当前目录
        2、如果不在当前目录，python则搜索在shell变量PYTHONPATH的每个目录
        3、如果都找不到，python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/

    模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH 和由安装过程决定的默认目录

模块导入问题
    相对导入使用模块的__name__属性来确定该模块在包层次结构中的位置。
    如果模块的名称不包含任何包信息(例如'__name__')，则相对导入将被视为该模块是顶级模块来进行解析，而不管模块实际位于文件系统上的什么位置
    通过断点查看每种情况下启动模块的__name__和__package__属性

    启动模块不要使用相对导入

__package__ == 'None' 问题
    __package__ == None ，导致查找不到起始脚本的路径，就无从判断当前脚本，对于sys.path中各路径的想对关系。
    解决办法
        修改sys.path，使其包含当前文件所在路径上想要想对的根目录，这时就可以根据这个目录确认想要引入的模块的路径了(这种办法是因为IDE没有自动匹配环境路径)
        这种办法由于是执行的时候才知道能不能找到对应的包，所以会提示错误。但是会执行成功
        并且这种办法中，from ... import ... 语句不是该模块第一个可执行语句，也会提示错误

        sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
        from moduleTest02 import bar01


python包的相对引用
    1.创建工程时，右键MARK AS source root
    2.里面放一个包，含__init__.py即可，这样就可将整个包导入环境变量中。os. path.append
    3.文件的引入使用相对引用.即可，from .. import Config, 主执行文件如果也用相对引用，就必须以模块身份运行，即python -m，如果以脚本方式运行，那么其包名为__main__, 只能使用绝对引用方式导入其它模块。
    4.下层包中的变量在引用时需要明确的从路径进行引用，from ..Lib import logger
    5.引用传递最好是向上传递，最好不在下层init.py中引用from .. import *

导入报错
    ImportError: attempted relative import beyond top-level package
        试图在顶级包之外进行相对导入
        原因：
            相对导入使用模块的__name__属性来确定该模块在包层次结构中的位置。
            如果模块的名称不包含任何包信息(例如'__name__')，则相对导入将被视为该模块是顶级模块来进行解析，而不管模块实际位于文件系统上的什么位置
            启动模块被调用的时候，__name__ == '__main__'，这个__name__不包含启动模块所在包的任何信息，所以启动模块会被当成顶级模块来进行解析，而不管模块实际位于文件系统什么位置
            非启动模块被调用的时候，__name__ == package1.package2.package3.module4。可以在被调用的各模块中输出__name__来查看
                例如：a02ProjectTest01.package1.module2

    ImportError: attempted relative import with no known parent package
        视图在没有已知父包的情况下进行相对导入
        原因：
            启动模块不要使用相对导入，应该使用绝对导入。
            非启动模块可以使用相对导入

    ModuleNotFoundError: No module named 'xxx'; 'xxx' is not a package
        没找到模块 'xxx'，'xxx'不是一个包
        原因：
            1、文件夹不是package，在文件夹添加__init__.py
            2、包中有和包名同名的.py文件

import注意事项整理
    1、工程下的文件夹名称以数字开头。无法被引用，也找不到路径。工程名、包名、模块名、函数名，不要以数字开头
    2、启动模块不要使用相对导入，应该使用绝对导入。非启动模块可以使用相对导入
    3、包文件夹添加__init__.py
    4、相对导入使用模块的__name__属性来确定该模块在包层次结构中的位置。
        如果模块的名称不包含任何包信息(例如'__name__')，则相对导入将被视为该模块是顶级模块来进行解析，而不管模块实际位于文件系统上的什么位置
        启动模块被调用的时候，__name__ == '__main__'，这个__name__不包含启动模块所在包的任何信息，所以启动模块会被当成顶级模块来进行解析，而不管模块实际位于文件系统什么位置
        非启动模块被调用的时候，__name__ == package1.package2.package3.module4。可以在被调用的各模块中输出__name__来查看
            例如：a02ProjectTest01.package1.module2

"""

"""
命名空间和作用域
    变量是拥有匹配对象的名字(标识符)。
    命名空间是一个包含了变量名称们(键)和它们各自相应的对象们(值)的字典。
    一个Python表达式可以访问局部命名空间和全局命名空间里的变量。
    如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
    每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。

    python会智能判断变量是局部还是全局的，它假设任何函数内赋值的变量都是局部的。
    因此：如果要给函数内的全局变量赋值，必须使用global语句

    global VarName 表达式声明变量是一个全局变量。
    例如：
        全局变量里定义一个变量Money，函数里给变量Money赋值，python会假定Money是一个局部变量。
        然而，并没有在访问前声明一个局部变量 Money，就会报错： UnboundLocalError
        解决办法：
            在给Money赋值前，使用 global Money 声明即可

"""

"""
模块相关函数
    dir(moduleName)
        以排序号的字符串列表形式，返回一个模块里定义过的名字
    globals()
        以字典的形式，返回全局命名空间里的名字
        如果在函数内部调用globals()，返回的是所有在改函数里能访问的全局名字
        可以使用keys()从globals()的结果获取键值
    locals()
        以字典的形式，返回局部命名空间里的名字
        在函数内部调用locals()，返回的是所有能在函数里访问的名字
        可以使用keys()从locals()的结果获取键值
    reload()
        当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
        如果想要重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块。
        语法：
            reload(module_name)

"""

print(__name__, __package__)
print(sys.path)
# moduleTest02.bar02.f()

# 全局变量&局部变量
Money = 2000


def AddMoney():
    global Money
    Money = Money + 1
    print("Money:", Money)

    # print("globals:",globals())
    # print("globals(keys):",globals().keys())
    # print("locals:",locals())
    # print("locals(keys):",locals().keys())


if __name__ == '__main__':
    print(__name__, __package__)
    function07()
    AddMoney()

    print(dir(b53ModLearn))

    # print("globals:",globals())
    # print("globals(keys):",globals().keys())
    # print("globals(keys)(type):",type(globals().keys()))
    # print("globals(keys)(type):",type(list(globals().keys())))
    # print("locals:",locals())
    # print("locals(keys):",locals().keys())
    # print("locals(keys)(type):",type(locals().keys()))
    # print("locals(keys)(type):",type(list(locals().keys())))

    reload(c03PackageTest01)
    
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

"""
Python面向对象
    Python从设计之初就已经是一门面向对象的语言，在Python中创建一个类和对象是很容易的。

面向对象技术简介
    类(Class)  
        用来描述具有相同属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量
        类变量在整个实例化的对象中是共用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员
        类变量或者实例变量，用于处理类及其实例对象的相关的数据
    方法重写
        如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖(override)，也称为方法的重写。
    局部变量
        定义在方法中的变量，只作用于当前实例的类
    实例变量
        在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
    继承
        即一个派生类(derived class)继承基类(base class)的字段和方法，继承也允许把一个派生类的对象作为一个基类对象对待。
        例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个(is-a)"关系
    实例化
        创建一个类的实例，类的具体对象。
    方法
        类中定义的函数
    对象
        通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法

创建类
    使用class语句创建一个新类，class之后为类的名称并以冒号结尾
    语法： 
        class ClassName:
            '类的帮助信息'    #类文档字符串
            class_suite     #类体

        类的帮助信息可以通过ClassName.__doc__查看
        class_suite由类成员，方法，数据属性组成

创建实例对象
    实例化类其他编程语言中一般用关键字new，但是在Python中并没有这个关键字，类的实例化类似函数调用方式
    以下使用类的名称Employee来实例化，并通过__init__方法接受参数
    样例：
        employee01 = Employee("renxiaowei",30)
        employee02 = Employee("dengtiejuan", 30)

访问属性
    使用点 . 来访问对象的属性。使用类的名称访问类变量
    样例：
        print(Employee.empCount,employee01.name,employee01.salary)
        print(Employee.empCount,employee01.name,employee01.salary)

    可以使用以下函数来访问属性
        getattr(obj, name[, default])  访问对象的属性
        hasattr(obj, name)  检查是否存在一个属性
        setattr(obj, name, value)  设置一个属性，如果属性不存在，会创建一个新属性
        delattr(obj, name)  删除属性

Python内置类属性
    __dict__   类的属性(包含一个字典，由类的数据属性组成)
    __doc__    类的文档字符串
    __name__   类名
    __module__ 类定义所在的模块(类的全名是 '__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于mymod)
    __bases__  类的所有父类构成函数(包含了一个由所有父类组成的元组)

Python对象销毁(垃圾回收)
    Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
    在Python内部记录着所有使用中的对象各有多少引用
    一个内部跟踪变量，称为一个引用计数器
    当对象被创建时，就创建了一个引用计数器，当这个对象不再需要时，也就是说，这个对象的引用计数变为0时，它被垃圾回收。
        但是回收不是"立即"的，由解释器在适当的时机，将垃圾对象占用的内存空间回收。

    样例    
        a = 40      #创建对象 <40>
        b = a       #增加引用，<40>的计数
        c = [b]     #增加引用，<40>的计数

        del a       #减少引用<40>的计数
        b = 100     #减少引用<40>的计数
        c[0] = -1   #减少引用<40>的计数

    垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。
    循环引用指的是，两个对象相互引用，但是没有其它变量引用他们。这种情况下，仅使用引用计数是不够的。
    Python的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。
    作为引用计数的补充，垃圾收集器也会留心被分配的总量很大(即未通过引用计数器销毁的那些)的对象。
    这种情况下，解释器会暂停下来，试图清理所有未引用的循环。

注意：
    通常需要在一个单独的文件中定义一个类

类的继承
    面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过集成机制
    通过集成创建的新类称为子类或派生类，被集成的类称为基类、父类、超类
    语法：
        class 派生类名(基类名)
            ...

    python中集成的一些特点
        1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。
        2、调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别在于类中调用普通函数时并不需要带上self参数
        3、Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。(先在本类中查找调用的方法，找不到在去基类中找)

    如果在集成元组中列了一个以上的类，那么它就被称作"多重继承"
    语法：
        class subClassName(ParentClass1[, ParentClass2, ...]):
            ...

继承判断方法
    issubclass(sub,sup)
        布尔函数，判断一个类是另一个类的子类或者孙类
    isinstance(obj,Class)
        布尔函数，判断obj是Class类的实例对象或者是一个Class子类的实例对象

方法重写
    如果父类的方法功能不能满足需求，可以在子类中重写父类的方法

基础重载方法
    下表列出了一些通用的功能，可以在自己定义的类中重写
    __init__(self[, args...])
        构造函数
        简单的调用方法
            obj = ClassName(args)

    __del__(self)
        析构函数，删除一个对象
        简单的调用方法
            del obj

    __repr__(self)
        转化为供解释器读取的形式
        简单的调用方法
            repr(obj)

    __str__(self)
        用于将值转化为适用于人阅读的形式
        简单的调用方法
            str(obj)

    __cmp__(self,x)
        对象比较
        简单的调用方法
            cmp(obj,x)

运算符重载
    Python支持运算符重载

类属性和方法
    类的私有属性
        __private_attrs: 两个下划线开头，声明该属性为私有属性，不能在类的外部被使用或直接访问。在类的内部方法中使用是 self.__private_attrs
        但是可以通过 object._ClassName__attrName(对象名._类名__私有属性名)访问属性
    类的方法
        在类的内部，使用def可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
        self可以替换成其它编码，例如：other
    类的私有方法
        __private_method:两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods

下划线说明
    头尾双下划线
        __foo__: 定义的是特殊方法，一般是系统定义名字，类似__init__()之类的
    单下划线
        _foo: 以单下划线开头的表示的是保护类型(protected)的变量，只能允许其本身与子类进行访问
        不能用于 from module import *
    双下划线
        __foo: 双下划线表示的是私有类型(private)的变量，只能允许这个类本身进行访问

理解
    对象在创建、删除、比较等操作的时候，会自动调用类内部一些自带的方法，例如：构造函数__init__，析构函数__del__，加法函数__add__，
    如果自带的这些函数的功能不是自己想要的，都是可以进行方法重载，方法覆盖，进行方法重写的。编写满足自己要求的功能。


"""


# 类练习
class Employee:
    "所有员工的基类"
    """
    empCount变量是一个类变量，它的值将在这个类的所有实例之间共享，可以在内部类或外部类使用Employee.empCount访问
    """
    empCount = 0

    """
    __init__()
        构造函数&初始化方法
        __init__()方法是一种特殊的方法，被称为类的构造函数或者初始化方法，当创建这个类的实例时就会调用该方法

    self:
        自己。代表类的实例本身
        self代表类的实例对象，而非类
        self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
        类内部，通过self调用类实例对象的属性及方法
        self相当于是构造函数的返回值

        注意：
            self 不是Python关键字，可以替换成其它名称

    """

    def __init__(self, name, salary):
        # 实例变量
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    """
    析构函数 __del__
        __del__ 在对象销毁的时候被调用，当对象不再被使用是，__del__方法运行
    """

    def __del__(self):
        className = self.__class__.__name__
        print("className:", className, ",销毁")

    """
    类方法
        类的方法和普通的函数只有一个特别的区别：他们必须有一个额外的第一个参数名称，按照惯例它的名称是self。
    """

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, ", salary:", self.salary)

    """
    self:代表类的实例，代表当前对象的地址
    self.__class__ 指向类
    """

    def prt(self):
        print(self)
        print(self.__class__)


# 类继承练习-父类
class Parent:
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性：", Parent.parentAttr)


# 类继承练习-子类
class Child(Parent):
    def __init__(self):
        print("调用子类构造函数")

    def childMethod(self):
        print("调用子类方法")

    def parendMethod(self):
        print("重写父类方法")


# 运算符重载练习
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 定义输出对象的时候按什么格式输出
    def __str__(self):
        return "Vector (%d, %d)" % (self.a, self.b)

    # 定义对象相加的时候如何计算
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


# 类属性&方法练习
class JustCounter:
    # 私有属性
    __secretCount = 0
    """
    类属性&公共属性
    可以用类名调用，可以用实例名调用，结果不一样
    """
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


if __name__ == '__main__':
    # #Employee() 标识调用Employee类的构造函数进行实例的创建
    # employee01 = Employee("renxiaowei",30)
    # employee01.displayCount()
    # employee01.displayEmployee()
    # employee01.prt()
    # print(Employee.empCount,employee01.name,employee01.salary)
    # employee02 = Employee("dengtiejuan", 30)
    # employee02.displayCount()
    # employee02.displayEmployee()
    # employee02.prt()
    # print(Employee.empCount,employee01.name,employee01.salary)
    #
    # #属性访问
    # print(hasattr(employee01, "name"))
    # print(getattr(employee01, "name"))
    # setattr(employee01, "name", "renxiaowei701")
    # print(getattr(employee01, "name"))
    # #delattr(employee01, "salary")
    # print(getattr(employee01, "salary"))
    #
    # #内置类属性
    # print("Employee.__dict__:",Employee.__dict__)
    # print("Employee.__doc__:",Employee.__doc__)
    # print("Employee.__name__:",Employee.__name__)
    # print("Employee.__module__:",Employee.__module__)
    # print("Employee.__bases__:",Employee.__bases__)
    #
    # #析构函数
    # #print(employee01,employee02)
    # #del employee01
    # #del employee02
    # employee03 = employee01
    # print(employee01,employee03)
    # del employee03
    # print(employee01)
    # del employee01

    # #继承练习
    # c = Child()
    # c.childMethod()
    # c.parendMethod()
    # c.setAttr(200)
    # c.getAttr()
    # print("Child是Parent的子类？",issubclass(Child,Parent))
    # print("c是Parent的实例？",isinstance(c,Parent))

    # #运算符重载
    # v1 = Vector(1,5)
    # v2 = Vector(2,3)
    # print(v1 + v2)

    # 类属性&方法练习
    jc = JustCounter()
    jc.count()
    jc.count()
    print(jc.publicCount)
    print(JustCounter.publicCount)
    # 可以通过 object._ClassName__attrName(对象名._类名__私有属性名)访问属性
    print(jc._JustCounter__secretCount)
    # print(jc.__secretCount)
    
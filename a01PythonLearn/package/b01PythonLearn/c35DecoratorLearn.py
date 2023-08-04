#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os

"""
装饰器
    装饰器(Decorators)是Python的一个重要部分。
    简单的说：他们是修改其他函数的功能的函数。
    有助于让代码更简单，更Pythonic(Python范儿)。
    需要知道在哪里使用装饰器，以及如何开发装饰器。
    
    用于修改其它函数的功能，对原函数进行功能扩展。
    一个函数可以被多个装饰器函数装饰。
    @symble 用@的方式对函数添加装饰器

    装饰器是得在一个函数的前后执行代码
    工厂模式？
    装饰器助力用更少、更简单的代码来实现复杂的逻辑，并在其他地方实现重用。

    装饰器就是定义一个嵌套函数，已一个函数作为参数，在嵌套函数中把参数函数前后加一下语句，然后把嵌套函数作为返回值。这样就相当于修改了参数函数的功能
    
    
注意：
    装饰器可以使用类的方式实现。在类中用下面的函数和标记实现装饰器类
    __call__
    @wraps(func)

装饰器包装
    functools.wraps 装饰器修饰函数 
    @wraps
        接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等功能。
        这可以让我们在装饰器里面访问在装饰之前的函数的属性

    @装饰器名称
        在函数前面加@+装饰器名称，表示使用指定的装饰器对该函数进行装饰。
        在后面使用该函数的是，就是已经经过装饰的功能了
        
装饰器参数

装饰器常用实现
    授权检查
    日志实现
    装饰器类
    发送邮件
    ...

装饰器定义及使用标准语句
    from functools import wraps
    def decorator_name(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not can_run:
                return "Function will not run"
            return f(*args, **kwargs)
        return decorated

    @decorator_name
    def func():
        return("Function is running")

    can_run = True
    print(func())
    # Output: Function is running

    can_run = False
    print(func())
    # Output: Function will not run

常见装饰器
    https://zhuanlan.zhihu.com/p/602457512
    @classmethod: 声明一个类方法，可以通过类名直接调用。
        python类中有三种方法类型：
            Instance methods(实例方法)：
                绑定一个实例的方法，利用这种方法可以访问和修改实例数据。
                通过类的实例调用实例方法，通过self参数访问实例数据。
                第一个参数是自身。
            Class methods(类方法)：
                @classmethod
                绑定一个类的方法，无法利用该方法修改实例数据。
                是调用类自身的一种方法，它将类作为第一个参数，通常将其命名为cls
            Static methods(静态方法)：
                @staticmethod
                不绑定实例或类的方法。仅仅因为他们在逻辑上属于那个类，才被包含进来。
                静态方法通常用于执行一组相关任务的使用程序类中，如数学计算。通过将相关函数组织成类的静态方法，使代码变得更加有组织、更容易理解。
                
    @staticmethod: 声明一个静态方法，可以通过类名直接调用。
    @property: 为Python类设置处理程序和设置程序。
        将一个方法转换为只读属性。也可以理解成，将一个方法改成了 __getter__方法。并且可以拿这个方法继续对后面的方法进行装饰。
        用于对属性进行保护
        Getters和Setters是面向对象编程（OOP）中的重要概念。
        对于类中的每个实例变量，getter方法返回其值，而setter方法设置或更新其值。鉴于此，Getters和Setters又分别称为Accessors和Mutators。
        它们用于保护数据不被直接意外访问或修改。
        不同的OOP语言有不同的机制来定义获取器getters和setters。在Python中，可以简单地使用@property装饰器。
        __getter__ __setter__
        
        通过property装饰后，可以直接取变量，也可以通过函数取变量。函数不能加()
    @abstractmethod: 声明一个抽象方法，子类必须实现它。
    
    @wraps: 用于保留原始函数的元数据（如函数名、注释等）。
        创建装饰器的时候使用。用于保留原始函数的元数据（如函数名、注释等）。
    
    @lru_cache：利用缓存提速程序。是提速Python函数最简易的方法
        此装饰器将函数的结果放入缓存，供后续具有相同参数的函数调用，无需再次执行具有相同参数的函数。
    @total_ordering: 填充缺失排序方法的类装饰器
        函数工具模块中的@total_sordeng装饰器为预定义Python类生成缺失比较方法。
        在类中没有对__ge__、__gt__和__le__方法进行定义。对该类的对象进行比较是会有问题。这个装饰器会补充缺失的比较方法
        一些旧的类可能未充分定义比较方法，将@total_ordering装饰器添加到其中之后，后续的使用更加安全。
    @contextmanager:定制的语境管理器
        可以使用with语句打开文件，在写入之后将自动关闭。无需显式地调用f.close（）函数来关闭该文件。
    @cached_property:将方法的结果作为属性放入缓存
        Python 3.8的函数工具模块引入了一个新的功能强大的装饰器-@cached_property，它将类的方法转换为一个属性，计算出该属性的值之后，将其作为实例的普通属性放入缓存。
    @dataclass:用更少的代码定义专用类
        （在Python3.7中引入）可以自动为一个类生成几种专用的方法，如__init__、__repr__、__eq__、__lt__等。
    @atexit.register:注册一个程序正常终止的函数
        atexit模块的@register装饰器允许在Python解释器退出时执行一个函数。
    
    
    @login_required: 用于限制需要用户登录才能访问的视图函数。
    @cache: 缓存函数的结果，避免重复计算。
    
    @retry: 在发生错误时自动重试代码块一定次数。
        需要自己定义

函数
    函数可以赋值
    函数中可以定义函数(函数中定义的函数，在函数外无法访问)
    函数可以返回函数

    funcName()  执行函数
        funcName()
    funcName    把函数整体赋值给另外一个变量
        a1 = funcName
        a1()
"""


"""
装饰器练习
"""
"""
装饰器函数定义
    functools.wraps 指明装饰的函数
@wraps(a01Fun)
    接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等功能。
        这可以让我们在装饰器里面访问在装饰之前的函数的属性
"""


def a01Decorator(a01Fun):
    @wraps(a01Fun)
    def wrapTheFunction():
        print("I am doing some boring work before executing a01Fun()")
        a01Fun()
        print("I am doing some boring work after executing a01Fun()")

    return wrapTheFunction


"""
@指明装饰器
在指明装饰器后，在使用函数的时候就可以直接使用装饰后的功能，不需要再使用装饰器进行包装赋值了
"""


@a01Decorator
def a02Fun():
    print("I am the function which needs some decoration to remove my foul smell")


"""
装饰器练习
"""


def decoratorLearn():
    a02Fun()
    print(a02Fun.__name__)
    # a03Fun = a01Decorator(a02Fun)
    # a03Fun()
    # print(a03Fun.__name__)
    return


"""
内置装饰器练习
"""
class IterClass:
    def __init__(self):
        self._score = 0

    @property
    def score1(self):
        return self._score

    @score1.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise Exception("参数太大，只允许0-100")


@dataclass
class Point:
    """@dataclass装饰器练习"""
    x: float
    y: float


def point_func():
    point = Point(1.0, 2.0)
    print(point)


"""自定义装饰器retry"""
def retry(max_retries=3, timeout=1):
    """
    https://pythonjishu.com/erfeaynjccecycp/
    定义装饰：用于函数重试，和等待重试时长。
    这里面的参数时装饰器函数本身的参数
    :param max_retries: 最大重试次数
    :param timeout: 设置超时重试时长
    :return:
    """
    def decorator(func):
        """
        定义装饰器和将装饰器返回
        :param func: 以函数式编程的方式，使用参数接收被装饰函数的函数名，在装饰器中使用 func() 进行执行函数
        :return: wrapper(被装饰之后的函数名，在函数被装饰之后，调用别装饰函数的时候，实际上调用的就是wrapper函数)
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            定义被装饰函数，被装饰之后的函数功能
            这里的参数时被装饰函数的参数
            @wraps(func): 这里可以使用wraps用来标识装饰器，并且接收func函数名。不写也可以
            @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
            :param args: (形参)(元组)用于接收被装饰函数的所有非关键字参数
            :param kwargs: (形参)(字典)用于接收被装饰函数的所有关键字参数
            :return:
            """
            """使用循环的方式对被装饰函数进行重试"""
            retries = 0
            exce_type = 0
            while retries < max_retries:
                try:
                    """
                    args: (实参)将通过wrapper函数接收到的被装饰函数的非关键字参数的参数集合(元组)，使用*进行展开，将其中所有元素单独传递给被装饰函数
                    kwargs: (实参)将通过wrapper函数接收到的被装饰函数的关键字参数的参数集合(字典)，使用**进行展开，将其中所有元素(键:值对)单独传递给被装饰函数
                    1、将被装饰函数所有参数传递给被装饰函数
                    2、执行被装饰函数
                    3、返回被装饰函数的return值(被装饰函数的返回值需要单独返回，要不然无法被引用)
                    注意点：
                        如果func执行没有异常，就会直接执行return语句将func结果返回，那就不会再进行循环了。而不会在func正常的情况下还将func循环执行三次
                    """
                    return func(*args, **kwargs)
                except BaseException as e:
                    """重试次数+1"""
                    retries += 1
                    """最后失败时，将失败原因进行保存，进行输出！"""
                    exce_type = e if retries == max_retries else None
                    """输出失败日志"""
                    print(f"执行 {func.__name__} 失败，正在进行第 {retries} 次重试！")
                    """失败重试，等待时间"""
                    time.sleep(timeout)
            """
            最终失败后将异常抛出，并且将失败信息进行提示！
            异常抛出的时候使用之前存储好的异常遍历，获取异常类型，准确的进行异常信息输出
            """
            raise exce_type.__class__(f"执行 {func.__name__} 失败，已达到最大重试次数，最终的失败原因是 {exce_type}！")
        """函数式编程:将被装饰器装饰后的的函数名返回"""
        return wrapper
    """函数式编程:将装饰器函数的函数名返回"""
    return decorator


@retry(max_retries=3, timeout=1)
def retry_test():
    """
    @retry: 使用装饰器retry对函数进行装饰
    max_retries: 传递给装饰器的参数
    timeout: 传递给装饰器的参数
    :return:
    """
    print("retry测试")
    raise(IOError, "主动抛出异常，用于装饰器测试！")
    return 1


@retry(max_retries=10, timeout=3)
def sum_num(x, y):
    a = x + y
    # raise (IOError, "主动抛出异常，用于装饰器测试！")
    return a


if __name__ == "__main__":
    # print("装饰器练习")
    # decoratorLearn()

    print("内置装饰器练习")
    ic = IterClass()
    ic.score = 10
    print(ic.score)
    print(ic.score1)
    ic.score = 100
    print(ic.score)
    print(ic.score1)

    point_func()

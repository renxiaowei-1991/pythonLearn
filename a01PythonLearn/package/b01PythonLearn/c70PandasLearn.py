#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

import pandas
import numpy

"""
1、pandas基础

pandas
    用于数据处理和分析的强大python库
    pandas.DataFrame(a_date) : 根据a_date的数据创建DataFrame二维表对象(a_date是字典格式)
    pandas.merge(pd_a, pd_b, on="姓名") : 使用merge函数关联pd_a和pd_b两个DataFrame对象，关联条件是"姓名"字段

numpy

Series
    一维数组对象
    可以使用list创建
        使用list创建series的时候可以指定index，index可以随便字段
    可以使用dict创建
        使用dict创建series的时候，指定的index必须和dict中的key相同，否则结果全部都是NaN

DataFrame
    创建空的 DataFrame
        df = pandas.DataFrame(columns=["Name", "Age", "Gender"])
    
    pandas.DataFrame(a_date)
        DataFrame对象创建
    pd_a["姓名"]
        从DataFrame对象pd_a中，取"姓名"字段
    pd_e[pd_e["年龄"] < 100]
        数据过滤，获取年龄小于100的数据
    pd_e.sort_values(by="年龄")
        数据排序: 返回排序后的结果，原数据不变
    pandas.DataFrame(f_date).fillna(-1)
        缺失值处理
        生成DataFrame的时候可以使用fillna对NaN值填充默认值
    pd_a.head(10)
        DataFrame对象输出的时候，默认只显示前5行，后5行。如果要查看其它行，需要使用head,tail指定
        显示前10行
    pd_a.tail(10)
        DataFrame对象输出的时候，默认只显示前5行，后5行。如果要查看其它行，需要使用head,tail指定
        显示后10行
    pd_a.drop(excludeColums, axis=1)
        从DataFrame删除指定列
        axis=0: 行
        axis=1: 列
        
    预览数据
        pd_a.head(10)
            DataFrame对象输出的时候，默认只显示前5行，后5行。如果要查看其它行，需要使用head,tail指定
            显示前10行
        pd_a.tail(10)
            DataFrame对象输出的时候，默认只显示前5行，后5行。如果要查看其它行，需要使用head,tail指定
            显示后10行
    
    数据过滤
        pd_e[pd_e["年龄"] < 100]
            数据过滤，获取年龄小于100的数据
    
    数据排序
        pd_e.sort_values(by="年龄")
            数据排序: 返回排序后的结果，原数据不变
    
    缺失值处理
        pandas.DataFrame(f_date).fillna(-1)
            生成DataFrame的时候可以使用fillna对NaN值填充默认值
        
    读取excel
        主要按照openpyxl，不需要import，但是需要按照。否则会报错。pandas会依赖openpyxl
        
        pandas.read_excel(base_path + "/table01.xlsx", sheet_name="Sheet1", skiprows=1, usecols=["dt", "_col1"], engine="openpyxl")
            读取指定excel文件
            sheet_name="Sheet1": 指定sheet页
            skiprows=1: 跳过指定行
            usecols=["dt", "_col1"]: 获取指定列(默认有列名)
            
            engine="openpyxl"
                指定excel处理的引擎
                xlrd, openpyxl, odf, pyxlsb
    
    读取csv
        csv实际上就是文本格式的excel
        读取csv不能指定sheet_name，csv默认只有一个sheet，也只能操作一个sheet。
        csv不需要指定skiprows，默认会跳过空格
        csv不需要指定usecols，实际上csv默认会把空行，空列都删除
    
    
    写入csv
        pd_a.to_csv(csv_file, encoding="utf-8", index=False)
            将DataFrame对象写入指定csv文件
            encoding="utf-8": 指定编码格式
            index=False: 不写索引列
        
    注意：
        DataFrame对象输出的时候，默认只显示前5行，后5行。如果要查看其它行，需要使用head,tail指定
"""


def pandas_series():
    """
    Series: 一维数组练习
    :return:
    """
    # 一维列表数据(列表)
    a_list = [1, 2, 3]
    # 一维列表数据(字典)
    a_dict = {"a": 1, "b": 2, "c": 3}

    # 根据list创建Series对象
    se_a_list = pandas.Series(a_list)
    # 使用list创建series的时候可以指定index，index可以随便字段
    # 使用dict创建series的时候，指定的index必须和dict中的key相同，否则结果全部都是NaN
    se_b_list = pandas.Series(a_list, index=["a", "b", "c"])
    print(se_a_list)
    print(se_b_list)
    # 根据dict创建Series对象
    se_a_dict = pandas.Series(a_dict)
    se_b_dict = pandas.Series(a_dict, index=["a", "b", "c"])
    se_b_dict_01 = pandas.Series(a_dict, index=["a", "b"])
    # 使用dict创建series的时候，指定的index必须和dict中的key相同，否则结果全部都是NaN
    se_c_dict = pandas.Series(a_dict, index=["x", "y", "z"])
    print(se_a_dict)
    print(se_b_dict)
    print(se_b_dict_01)
    print(se_c_dict)

    return


def pandas_dataframe():
    """
    DataFrame: 二维数组练习
    :return:
    """
    # 创建空的 DataFrame
    df = pandas.DataFrame(columns=["Name", "Age", "Gender"])

    # a表数据
    a_date = {
        "姓名": ["孙悟空", "猪八戒", "沙悟净", "唐僧"],
        "名称": ["齐天大圣", "天蓬元帅", "沙和尚", "唐三藏"]
    }

    # b表数据
    b_date = {
        "姓名": ["孙悟空", "猪八戒", "沙悟净", "唐僧"],
        "职称": ["大师兄", "二师兄", "三师弟", "师傅"]
    }

    # c表数据
    c_date = {
        "姓名": ["孙悟空", "猪八戒", "沙悟净", "唐僧"],
        "年龄": [1500, 2000, 2000, 40]
    }

    # 生成a表的DataFrame
    pd_a = pandas.DataFrame(a_date)
    # 生成b表的DataFrame
    pd_b = pandas.DataFrame(b_date)
    # 生成b表的DataFrame
    pd_c = pandas.DataFrame(c_date)

    # 打印对象
    print("打印对象")
    print("pd_a: ", type(pd_a), "数据：\n", pd_a) # class 'pandas.core.frame.DataFrame'
    print("pd_b: ", type(pd_b), "数据：\n", pd_b) # class 'pandas.core.frame.DataFrame'
    print("pd_a['姓名']: ", type(pd_a["姓名"]), "数据：\n", pd_a["姓名"]) # class 'pandas.core.series.Series'
    print("pd_b['职称']: ", type(pd_b["职称"]), "数据：\n", pd_b["职称"]) # class 'pandas.core.series.Series'

    # a表和b表通过姓名字段关联合并
    df_d = pandas.merge(pd_a, pd_b, on="姓名")
    print("打印对象：合并")
    print("df_d: ", type(pd_a), "数据：\n", df_d)  # class 'pandas.core.frame.DataFrame'
    print("df_d['姓名']: ", type(df_d["姓名"]), "数据：\n", df_d["姓名"])  # class 'pandas.core.series.Series'

    # 数据过滤
    # a表和c表通过姓名关联合并，然后按照年龄过滤数据
    pd_e = pandas.merge(pd_a, pd_c, on="姓名")
    print(pd_e["年龄"] < 100)
    print(pd_e[pd_e["年龄"] < 100])

    # 数据排序: 返回排序后的结果，原数据不变
    print(pd_e.sort_values(by="年龄"))
    print(pd_e)

    # 缺失值处理
    # f表数据
    f_date = {
        "姓名": ["孙悟空", "猪八戒", "沙悟净", "唐僧"],
        "年龄": [1500, 2000, numpy.NAN, 40]
    }
    # 生成f表的DataFrame
    # 生成DataFrame的时候可以使用fillna对NaN值填充默认值
    pd_f = pandas.DataFrame(f_date).fillna(-1)
    print(pd_f)

    return


def pandas_dataframe_excel():
    """
    读取excel
    :return:
    """
    base_path = r"D:\02helloWorld\03Python\a01pythonLearn\excel"
    # 读取指定excel文件
    # 指定sheet页: sheet_name="Sheet1"
    # skiprows=1: 跳过指定行
    # usecols=["dt", "_col1"]: 获取指定列(默认有列名)
    pd_a = pandas.read_excel(base_path + "/table01.xlsx", sheet_name="Sheet1", skiprows=1, usecols=["dt", "_col1"], engine="openpyxl")
    print(pd_a)
    # 预览数据
    # 显示前10行
    print(pd_a.head(10))
    # 显示后10行
    print(pd_a.tail(10))

    return


def pandas_dataframe_csv():
    """
    读取csv
    :return:
    """
    base_path = r"D:\02helloWorld\03Python\a01pythonLearn\excel"
    """
    csv实际上就是文本格式的excel
    读取csv不能指定sheet_name，csv默认只有一个sheet，也只能操作一个sheet。
    csv不需要指定skiprows，默认会跳过空格
    csv不需要指定usecols，实际上csv默认会把空行，空列都删除
    """
    pd_a = pandas.read_csv(base_path + "/table01.csv", usecols=["dt", "_col1"])

    print(pd_a)
    return


def pandas_excel_to_csv(excel_file, csv_file, sheet="Sheet1", skiprow=0, includeColums=[], excludeColums=[]):
    """
    将指定excel文件中，指定sheet页，按条件获取数据，保存到csv文件中
    :param excel_file: excel来源文件
    :param csv_file: csv目标文件
    :param sheet: excel获取sheet页
    :param skiprows: 读取跳过行数
    :param includeColums: excel读取获取列
    :param excludeColums: excel读取排除列
    :return:
    """
    pd_a = pandas.read_excel(excel_file, sheet_name=sheet, skiprows=skiprow, usecols=includeColums)
    print(pd_a)
    # 排除列不为空的时候执行下述操作
    if excludeColums:
        # 从DataFrame删除指定列
        # axis=1: 列
        # axis=0: 行
        try:
            pd_a.drop(excludeColums, axis=1)
        except BaseException as be:
            print("排除列异常，异常原因：", be.__class__, be)

    # 将DataFrame对象写入指定csv文件
    # encoding="utf-8": 指定编码格式
    # index=False: 不写索引列
    pd_a.to_csv(csv_file, encoding="utf-8", index=False)
    print("excel转csv成功")
    return


"""
2、数据处理

2.1、数据查看
查看pandas_data_view()函数

2.1.1、数据预览
    head(): 预览数据的前几行，以了解数据的整体结构和格式
    tail(): 预览数据的后几行，以了解数据的整体结构和格式
2.1.2、信息查看
    info(): 查看数据所有基本信息
    info: 查看数据
    shape: 查看数据行数&列数
    df.sample(2, axis=0) : 随机查看(2行)
    df.sample(2, axis=1) : 随机查看(2列)
        axis=0: 表示行
        axis=1: 表示列
    df.dtypes: 查看每一列的数据类型
    df["日期"].dtypes: 查看指定列的数据类型
2.1.3、基本统计量
    describe(): 获取数据的基本统计信息，如均值、标准差、最小值、最大值等，帮助了解数据的分布和范围
    
    其它统计函数: 等同于describe的一部分
        mean(): 计算每列数据平均值
        median(): 计算每列数据中位数
        sum(): 计算每列数据总和
        min(): 计算每列数据最小值
        max(): 计算每列数据最大值
        std(): 计算每列数据标准差
        var(): 计算每列数据方差
        count(): 计算每列数据非缺失值数量
        quantile(): 计算每列数据指定分位数
            样例: df["销售金额"].quantile(25 / 100) # 25%位置的数
        corr(): 计算每列数据之间的相关系数(相关性分析)
            查看pandas_corr()函数
            
            需要安装模块 scipy
            pearman: 斯皮尔曼相关系
            kendall: 肯德尔相关系数
            样例：
                print(df["销售金额"].corr(df["销售金额"], method="spearman"))
                自相关，相关性是1
        
2.1.4、唯一值与计数
    了解数据的分类和频率分布
    unique(): 获取列中的唯一值。
    value_counts(): 获取各个值的计数
    参数：
        normalize: 如果设置为True，则返回的计数以相对频率(百分比的形式)的形式显示，而不是绝对计数。默认值为False
        sort: 如果设置为True，则按计数值的降序对结果进行排序。默认值为True
        ascending: 如果设置为True，则按计数值的升序对结果进行排序，默认值为False
        dropna: 如果设置为False，则不会忽略(NAN)，并将其视为一个独立的类别。默认值为True，即忽略缺失值
    样例：
        print(df_a["颜色"].value_counts(normalize=True))
        print(df_a["颜色"].value_counts(sort=True))
        print(df_a["颜色"].value_counts(ascending=True))
        print(df_a["颜色"].value_counts(dropna=True))
    
2.1.5、缺失值检测
查看pandas_handle_nan()函数

    了解数据完整性
    isnull(): 检测数据中的缺失值。返回一个布尔型的DataFrame，标记了数据中的缺失值位置。对于缺失值位置，返回True，对于非缺失值位置，返回False
    notnull(): 检测数据中的非缺失值。返回一个布尔型的DataFrame，标记了数据中的非缺失值位置，对于非缺失值位置，返回True，对于缺失值位置，返回False
    isna(): isnull()的别名函数，执行相同的操作
    notna(): notnull()的别名函数，执行相同的操作
    any(): 检测DataFrame或Series对象中是否存在任何缺失值，返回一个布尔型值，如果存在缺失值，则为True，否则为False
    all(): 检测DataFrame或Series对象中的所有值是否都是缺失值，返回一个布尔值，如果所有值都是缺失值，则为True，否则为False
    
    sum(): 统计每列的数量，配合isnull() 可以统计每列缺失值数量
    
2.1.6、空字符检测&处理了
    空字符
        一个空格&多个空格
        一个tab&多个tab
        一个换行&多个换行
        各种空字符同时出现
    
    检测空字符
        print(df_b[df_b["销售金额"] == " "])
    
    删除空字符
        df["销售金额"] = df["销售金额"].replace(r"[ \n\t]", "")
        df["销售金额"] = df["销售金额"].replace(r"[\s]", "") # \s匹配空字符(空格、换行、tab)
        
        df["text"] = df["text"].replace(r"[ \n\t]*", "", regex=True)
        df["text"] = df["text"].replace(r"\s", "", regex=True)
            regex=True: 表示支持正则表达式
        df["text"] = df["text"].replace("", np.NAN)
            将空字符替换成缺省值
            
    将缺省值替换为指定值
        df["text"]  = df["text"].fillna(-1)
        
    注意：
        不能直接将空字符替换成缺省值。否则会导致包含空支付的字符串都变成缺省值。
        任何字符串和缺失值连接都是缺省值
        df["text"] = df["text"].replace(r"[ \n\t]*", numpy.NAN, regex=True)

2.2、数据清洗
2.2.1、处理缺失值
    查看pandas_handle_nan_01()函数
    
    dropna(): 删除包含缺失值的行或列
        thresh=n: 保留至少有n个非NaN数据的行/列
        inplace=True: 直接修改原数据
    fillna(): 填充缺失值，选择适当的方法取决于具体的数据情况
        inplace=True: 在原位置替换，不需要重新赋值。可以修改原数据。如果不加这个参数需要使用赋值的方式修改原数据
        method="ffill": 填充前一个的值
        method="bfill": 填充后一个的值
        注意：处理Series和DataFrame都需要加inplace才可以直接修改原数据。之前参考的样例有错误
2.2.2、处理重复值
    查看pandas_duplicate()函数
    
    duplicated(): 检测重复值
    drop_duplicates(): 删除重复值，确保数据的唯一性
        subset: 指定在哪些列中检查重复值，可以是单个列名的字符串或包含多个列名的列表
        keep: 指定保留哪个重复值，可选值包括"first","last","False"
        inplace: 指定是否在原始对象上进行就地删除。默认为False
        ignore_index: 重置索引，使删除重复值后的DataFrame的索引连续增加
        subset_keep: 为每个指定的列提供一个保留方式的字典。可以用于为不同的列指定不同的保留方式。
2.2.3、处理异常值
    查看pandas_handle_abnormal()函数
    
    通过使用可视化工具和基本统计分析来识别和处理异常值，可以使用过滤、替换或删除等方法来应对异常值
    数据过滤
        df[((df["颜色"] == "") | df["颜色"].isna())]
        注意：
            过滤条件联合，不能使用and or。需要使用 | &
    数据替换
        1、找出需要替换的数据所在行的过滤条件
          ((df["颜色"] == "") | df["颜色"].isna())
        2、按过滤条件过滤后的数据中，指定要处理的行，以及替换后的数据
          df.loc[条件, 要替换的列] = 要替换的值
        样例：
            df.loc[((df["颜色"] == "") | df["颜色"].isna()), "颜色"] = "黑色"
    数据删除
        df[条件] 找到符合条件的行
        df[条件]: 结果使存储True&False的Series。包含索引+数据列
        1、利用取反~，达到删除的效果
        2、df.drop(df[条件].index, inplace=True)
            根据行索引删除，修改原数据
            df.drop(df[(df["颜色"] == "") | df["颜色"].isna()].index, inplace=True)
        3、df.drop([要删除行的索引列表], inplace=True)
            df.drop([3, 5], inplace=True)
2.2.4、数据类型转换
    查看pandas_handle_type()函数
    
    基础类型转换
        astype(): 将列的数据类型转换为正确的类型，确保数据的一致性和准确性
        df["B"].astype(int)
            转换类型后汇总: df["B"].astype(int).sum()

    日期类型转换
        pandas.to_datetime(df["A"], format="%Y-%m")
            format="%Y-%m": 指定datetime类型转换格式
2.2.5、数据格式化与规范化
    查看pandas_handle_standard()函数
    
    对于字符串类型的数据，可以使用字符串处理函数，对数据进行格式化和规范化
    str.lower(): 转小写
    str.upper(): 转大写
    str.strip(): 去除空格

2.3、数据预处理
2.3.1、特征选择与删除
    根据分析目标和特征的相关性，选择相关特征并删除不相关或冗余的特征，以提高后续分析的效果。
    
    特征选择：比如一个excel中有多列的数据，但是我们只需要某些列。那么可以选择指定的列进行使用
    loc: 可以选择具体的索引
    
    df[["A", "B"]]: 选择A列+B列
    df["A"]: 选择A列
    df.loc[1:3]
    df.loc[1:3, "A"]
    df.loc[1:3, ["A", "B"]]
    
    
    
2.3.2、数据转换与衍生
    使用apply()函数或自定义函数对数据进行转换和衍生，如：特征缩放、数值转换、日期提取等，以适应不同的分析需求
    apply()
2.3.3、数据合并与拆分
    通过使用merge()函数或concat()函数，可以将多个数据集合并成一个，或将一个数据集拆分成多个，以满足数据分析的需求
    merge(): 合并数据集
    concat(): 
2.3.4、数据重塑与透视
    使用pivot()函数或melt()函数，可以对数据进行重塑和透视，以更好地理解和分析数据的关系和趋势
    pivot()
    melt()
"""
def pandas_data_view():
    """
    数据查看练习
    :return:
    """
    base_path = r"D:\02helloWorld\03Python\a01pythonLearn\excel"
    # 读取excel数据文件
    df = pandas.read_excel(base_path + "/销售数据.xlsx", sheet_name="Sheet1", usecols=["日期", "销售金额"], engine="openpyxl")
    # 数据预览
    print(df.head(5)) # 查看前5行
    print(df.tail(5)) # 查看后5行
    # 信息查看
    print(df.info) # 查看数据
    print(df.info()) # 查看数据所有基本信息
    print(df.shape) # 查看数据行数&列数
    # 随机抽查
    print(df.sample(2, axis=0)) # 随机查看两行
    print(df.sample(2, axis=1)) # 随机查看两列
    # 查看数据类型
    print(df.dtypes) # 查看每一列的数据类型
    print(df["日期"].dtypes) # 查看指定列的数据类型

    # 基本统计量
    print(df.describe()) # 查看数据基本统计信息(均值、标准差、最小值、最大值等)
    print(df["销售金额"].mean()) # 计算每列数据平均值
    print(df["销售金额"].median()) # 计算每列数据中位数
    print(df["销售金额"].sum()) # 计算每列数据总和
    print(df["销售金额"].min()) # 计算每列数据最小值
    print(df["销售金额"].max()) # 计算每列数据最大值
    print(df["销售金额"].std()) # 计算每列数据标准差
    print(df["销售金额"].var()) # 计算每列数据方差
    print(df["销售金额"].count()) # 计算每列数据非缺失值数量
    print(df["销售金额"].quantile(25 / 100)) # 计算每列数据指定分位数
    # 需要安装模块 scipy
    # spearman: 斯皮尔曼相关系数
    # kendall: 肯德尔相关系数
    print(df["销售金额"].corr(df["销售金额"], method="spearman"))

    # 唯一值与计数
    df_a = pandas.read_excel(base_path + "/销售数据.xlsx", sheet_name="Sheet2", usecols=["角色", "颜色"])
    print(df_a)
    # 统计唯一值
    print(df_a["角色"].unique())
    # 统计重复次数
    # 参数：
    #   normalize: 如果设置为True，则返回的计数以相对频率(百分比的形式)的形式显示，而不是绝对计数。默认值为False
    #   sort: 如果设置为True，则按计数值的降序对结果进行排序。默认值为True
    #   ascending: 如果设置为True，则按计数值的升序对结果进行排序，默认值为False
    #   dropna: 如果设置为False，则不会忽略(NAN)，并将其视为一个独立的类别。默认值为True，即忽略缺失值
    print(df_a["颜色"].value_counts())
    print(df_a["颜色"].value_counts(normalize=True))
    print(df_a["颜色"].value_counts(sort=True))
    print(df_a["颜色"].value_counts(ascending=True))
    print(df_a["颜色"].value_counts(dropna=True))

    return


def pandas_handle_nan():
    """
    空字符&缺失值处理
    :return:
    """
    base_path = r"D:\02helloWorld\03Python\a01pythonLearn\excel"
    # 读取excel数据文件
    df = pandas.read_excel(base_path + "/销售数据.xlsx", sheet_name="Sheet1", usecols=["日期", "销售金额"], engine="openpyxl")

    # 缺失值检测
    base_path = r"D:\02helloWorld\03Python\a01pythonLearn\excel"
    # 读取excel数据文件
    df_b = pandas.read_excel(base_path + "/销售数据.xlsx", sheet_name="Sheet3", usecols=["日期", "销售金额"], engine="openpyxl")
    # df_b["销售金额"][8] = ""

    # isnull(): 检测数据中的缺失值。返回一个布尔型的DataFrame，标记了数据中的缺失值位置。对于缺失值位置，返回True，对于非缺失值位置，返回False
    # notnull(): 检测数据中的非缺失值。返回一个布尔型的DataFrame，标记了数据中的非缺失值位置，对于非缺失值位置，返回True，对于缺失值位置，返回False
    # isna(): isnull()
    # 的别名函数，执行相同的操作
    # notna(): notnull()
    # 的别名函数，执行相同的操作
    # any(): 检测DataFrame或Series对象中是否存在任何缺失值，返回一个布尔型值，如果存在缺失值，则为True，否则为False
    # all(): 检测DataFrame或Series对象中的所有值是否都是缺失值，返回一个布尔值，如果所有值都是缺失值，则为True，否则为False
    print(df_b.head(12))
    print(df_b["销售金额"].isnull())
    print(df_b["销售金额"].isna())
    print(df_b["销售金额"].notnull())
    print(df_b["销售金额"].notna())
    print(df_b["销售金额"].isnull().all())
    print(df_b["销售金额"].notnull().all())
    print(df_b["销售金额"].isnull().any())
    print(df_b["销售金额"].notnull().any())
    print(df_b["销售金额"].all())
    print(df_b["销售金额"].all())
    print(df_b["销售金额"].any())
    print(df_b["销售金额"].any())

    # 空字符检测
    #   一个空格&多个空格
    #   一个tab&多个tab
    #   一个换行&多个换行
    #   各种空字符同时出现
    print("\n\n\n")
    print(df_b[df_b["销售金额"] == " "])
    # 删除空字符
    df["销售金额"] = df["销售金额"].replace(r"[ \n\t]", "")
    df["销售金额"] = df["销售金额"].replace(r"[\s]", "")  # # \s匹配空字符(空格、换行、tab)
    print(df["销售金额"])

    data = {"text": [" \t\n", " \nWorld\n", "\tWelcome"]}
    df = pandas.DataFrame(data)
    # regex=True: 表示支持正则表达式
    df["text"] = df["text"].replace(r"[ \n\t]*", "", regex=True)
    print(df["text"])
    df["text"] = df["text"].replace("", numpy.NAN)
    df["text"]  = df["text"].fillna(-1)
    # 不能直接将空字符替换成缺省值。否则会导致包含空支付的字符串都变成缺省值。
    # 任何字符串和缺失值连接都是缺省值
    # df["text"] = df["text"].replace(r"[ \n\t]*", numpy.NAN, regex=True)
    print(df["text"])
    print("\n\n\n")
    print(str(numpy.NAN) + "aaa")
    return


def pandas_corr():
    """
    相关性分析
    :return:
    """
    data_a = {
        "月份": [1, 2, 3, 4, 5, 6],
        "销售金额": [100, 120, 110, 130, 140, 150],
        "广告费用": [500, 600, 550, 700, 800, 900],
    }
    df = pandas.DataFrame(data_a)
    # 销售金额&广告费用 正相关，相关性：0.9999999999999999
    print(df["销售金额"].corr(df["广告费用"], method="kendall"))

    data_b = {
        "月份": [1, 2, 3, 4, 5, 6],
        "销售金额": [100, 90, 80, 70, 60, 50],
        "广告费用": [500, 600, 550, 700, 800, 900],
    }
    df = pandas.DataFrame(data_b)
    # 销售金额&广告费用 负相关，相关性：-0.8666666666666666
    # 分析方法默认：spearman: 斯皮尔曼相关系数
    print(df["销售金额"].corr(df["广告费用"]))
    return


def pandas_handle_nan_01():
    """
    处理空字符&空字符串&缺失值
    :return:
    """
    base_path = r"D:\02helloWorld\03Python\a01pythonLearn\excel"
    # 读取excel数据文件
    df = pandas.read_excel(base_path + "/销售数据.xlsx", sheet_name="Sheet3", usecols=["日期", "销售金额"])

    # 替换空字符
    df["销售金额"] = df["销售金额"].replace(r"\s", "", regex=True)
    # 空字符串替换为NAN
    df["销售金额"] = df["销售金额"].replace("", numpy.NAN)

    # 对象复制，重复练习
    #   注意：不能直接将df赋值给df_a，直接赋值是对象的引用，还是指向同一个对象。使用copy复制出来的就是两个对象了
    # df_a = df_b = df_c = df.copy()
    df_a = df.copy()
    df_b = df.copy()
    df_c = df.copy()

    # 缺失值填充指定值
    # 将指定列的缺省值(NAN)填充为-1.有两种办法
    #   填充后赋值给原列，如果不赋值，不会修改原数据
    # df["销售金额"] = df["销售金额"].fillna(-1)
    #   直接使用参数inplace进行填充，不需要赋值，可以直接修改DataFrame数据
    # df["销售金额"].fillna(-1, inplace=True)

    # 将所有列的缺省值(NAN)填充为-1.有两种办法
    #   填充后赋值给原列，如果不赋值，不会修改原数据
    # df = df.fillna(-1)
    #   直接使用参数inplace进行填充，不需要赋值，可以直接修改DataFrame数据
    df.fillna(-1, inplace=True)
    print(df)

    # 填充前一个的值
    #   替换的时候也是有两种方法。一种是使用赋值的方式，一种是使用inplace的方式直接修改
    print(df_a)
    df_a.fillna(method="ffill", inplace=True)
    print(df_a)

    # 填充后一个的值
    #   替换的时候也是有两种方法。一种是使用赋值的方式，一种是使用inplace的方式直接修改
    print(df_b)
    df_b.fillna(method="bfill", inplace=True)
    print(df_b)

    # 删除缺省值:dropna
    #   thresh: 保留至少有n个非NaN数据的行/列
    #   inplace=True: 直接修改原数据
    print("\n\n\n", df_c)
    # df_c.dropna(inplace=True)
    # df_c.dropna()
    df_c.dropna(thresh=2, inplace=True)
    print(df_c)

    # Series测试，缺省值填充前一个值
    df_s = pandas.Series([1, None, 3, None, 5])
    print("\n\n\n", df_s)
    df_s.fillna(method="ffill", inplace=True)
    print(df_s)

    return


def pandas_duplicate():
    """
    重复值处理
    :return:
    """
    df = pandas.DataFrame(
        {
            "A": [1, 2, 3, 2, 8, 8],
            "B": [1, 6, 7, 6, 8, 7]
        }
    )
    print(df)
    # 检查重复值
    print(df.duplicated())
    # 判断是否有重复值
    print(df.duplicated().all())
    # 删除重复值
    #   subset: 指定在哪些列中检查重复值，可以是单个列名的字符串或包含多个列名的列表
    #   keep: 指定保留哪个重复值，可选值包括"first","last","False"
    #   inplace: 指定是否在原始对象上进行就地删除。默认为False
    #   ignore_index: 重置索引，使删除重复值后的DataFrame的索引连续增加
    #   subset_keep: 为每个指定的列提供一个保留方式的字典。可以用于为不同的列指定不同的保留方式。
    # print(df.drop_duplicates())
    # 同时看A/B列重复值删除
    # print(df.drop_duplicates(subset=["A", "B"]))
    # 只根据A列重复值删除，删除重复值中后一个值
    print(df.drop_duplicates(subset=["A"], keep="last"))

    return


def pandas_handle_abnormal():
    """
    异常值处理
        数据过滤:
            df[((df["颜色"] == "") | df["颜色"].isna())]
            df[~((df["颜色"] == "") | df["颜色"].isna())]
        数据替换
            1、找出需要替换的数据所在行的过滤条件
                ((df["颜色"] == "") | df["颜色"].isna())
            2、按过滤条件过滤后的数据中，指定要处理的行，以及替换后的数据
                df.loc[条件, 要替换的列] = 要替换的值
        数据删除
            df[条件] 找到符合条件的行
            df[条件]: 结果使存储True&False的Series。包含索引+数据列
            1、利用取反~，达到删除的效果
            2、df.drop(df[条件].index, inplace=True)
                根据行索引删除，修改原数据
            3、df.drop([要删除行的索引列表], inplace=True)
    :return:
    """
    data = {
        "角色": ["刘备", "关羽", "张飞", "赵云", "黄忠", "马超", "曹操", "孙权", "周瑜"],
        "颜色": ["红色", "绿色", "蓝色", "", "红色", numpy.NAN, "蓝色", "黄色", "红色"]
    }
    df = pandas.DataFrame(data)
    # 数据过滤
    print(df)
    print("\n\n\n", df[((df["颜色"] == "") | df["颜色"].isna())])
    # ~ 取反
    print("\n\n\n", df[~((df["颜色"] == "") | df["颜色"].isna())])

    # 数据替换
    #   1、找出需要替换的数据所在行的过滤条件
    #     ((df["颜色"] == "") | df["颜色"].isna())
    #   2、按过滤条件过滤后的数据中，指定要处理的行，以及替换后的数据
    #     df.loc[条件, 要替换的列] = 要替换的值
    df.loc[((df["颜色"] == "") | df["颜色"].isna()), "颜色"] = "黑色"
    print("\n\n\n", df)

    # 数据删除
    df = pandas.DataFrame(data)
    # df[条件] 找到符合条件的行
    #   df[条件]: 结果使存储True&False的Series。包含索引+数据列
    # 1、利用取反~，达到删除的效果
    # 2、df.drop(df[条件].index, inplace=True)
    #   根据行索引删除，修改原数据
    # 3、df.drop([要删除行的索引列表], inplace=True)
    print(type((df["颜色"] == "") | df["颜色"].isna()))
    print(df[(df["颜色"] == "") | df["颜色"].isna()].index)
    # 根据索引删除
    # df.drop([3, 5], inplace=True)
    # 根据判断条件删除
    df.drop(df[(df["颜色"] == "") | df["颜色"].isna()].index, inplace=True)
    print("\n\n\n", df)
    return


def pandas_handle_type():
    """
    数据类转换
        基本类型转换: astype(int)
        日期类型转换: pd.to_datetime()
            format="%Y-%m": 指定datetime类型转换格式
    :return:
    """
    df = pandas.DataFrame({
        "A": ["2023-01", "2023-02", "2023-03"],
        "B": ["100", "100", "200"]
    })
    print(df.info())

    # 基础类型转换
    # 获取字典类型
    print(df["B"].dtype)
    # 按原字典类型汇总
    print(df["B"].sum())
    # 转换类型后汇总
    print(df["B"].astype(int).sum())

    # 日期类型转换
    print(df["A"].dtype)
    # 日期格式就是按照datetime格式化日期格式处理
    #   通过.dt获取datetime格式日期
    print(pandas.to_datetime(df["A"], format="%Y-%m"))
    print(pandas.to_datetime(df["A"], format="%Y-%m").dt.year)
    print(pandas.to_datetime(df["A"], format="%Y-%m").dt.month)
    print(pandas.to_datetime(df["A"], format="%Y-%m").dt.day)
    print(df)
    print(df.info())

    return


def pandas_handle_standard():
    """
    数据格式化&规范化
        str.lower
        str.upper
        str.strip
    :return:
    """
    df = pandas.DataFrame({
        "Name": [" John Smith ", "Mary Johnson", " David Brown "]
    })
    print(df)
    # 转小写
    print(df["Name"].str.lower())
    # 转大写
    print(df["Name"].str.upper())
    # 去空格
    print(df["Name"].str.strip())

    return


def pandas_handle_data():
    """
    2.3、数据预处理
    查看pandas_handle_data()函数

    2.3.1、特征选择与删除
        根据分析目标和特征的相关性，选择相关特征并删除不相关或冗余的特征，以提高后续分析的效果。

        特征选择：比如一个excel中有多列的数据，但是我们只需要某些列。那么可以选择指定的列进行使用
        loc: 可以选择具体的索引

        df["A"]: 选择A列
        df[["A", "B"]]: 选择A列+B列
        df.loc[1]: 不指定列，选择所有列，索引1行
        df.loc[1:3]: 不指定列，选择所有列，索引1-3行
        df.loc[1:3, "A"]: 选择A列，索引1-3行
        df.loc[1:3, ["A", "B"]]: 选择A列+B列，索引1-3行

    2.3.2、数据转换与衍生
        使用apply()函数或自定义函数对数据进行转换和衍生，如：特征缩放、数值转换、日期提取等，以适应不同的分析需求
        apply()

        数据衍生-增加行
        方法一：通过索引的方式增加行，值按照列表指定。值按照字段顺序 姓名、年龄、爱好
            df.loc[len(df)] = ["诸葛亮", 55, "计谋"]
        方法二：通过索引的方式增加行，值根据字典指定
            df.loc[len(df)] = {"Name": "任小伟", "Age": 1024, "Gender": "学习"}
        方法三：通过pandas.concat([])拼接DataFrame
            df_a = pandas.concat([df, df], ignore_index=True)

    2.3.3、数据合并与拆分
        通过使用merge()函数或concat()函数，可以将多个数据集合并成一个，或将一个数据集拆分成多个，以满足数据分析的需求
        merge(): 关联合并数据集
        concat(): union合并数据集
            df_a = pandas.concat([df, df], ignore_index=True)
    2.3.4、数据重塑与透视
        使用pivot()函数或melt()函数，可以对数据进行重塑和透视，以更好地理解和分析数据的关系和趋势
        pivot()
        melt()
    :return:
    """
    df = pandas.DataFrame({
        "年龄": [25, 30, 35, 40],
        "性别": ["男", "女", "男", "女"],
        "收入": [50000, 60000, 70000, 80000],
        "购买历史": ["是", "否", "是", "否"],
        "目标": [1, 0, 1, 0]
    })
    print(df)

    # 2.3.1 特征选择与删除
    selected_features = ["年龄", "收入", "购买历史"]
    # 选择指定列
    print(df[selected_features])
    # 按索引选择行，索引列
    print(df.loc[1])
    # 按索引选择行，所有列
    print(df.loc[1:3])
    # 选择指定列，按所有选择行
    print(df.loc[1:3, selected_features])

    # 2.3.2 数据转换与衍生
    df = pandas.DataFrame({
        "A": ["2023-01", "2023-02", "2023-03"],
        "B": ["100", "100", "200"]
    })
    print(df.info())
    # 数据转换
    df["A"] = pandas.to_datetime(df["A"], format="%Y-%m")
    print(df["A"].dt.year)
    print(df)

    # 数据衍生-增加行
    # 创建空的 DataFrame
    df = pandas.DataFrame(columns=["Name", "Age", "Gender"])
    print(df)
    # 方法一：通过索引的方式增加行，值按照列表指定。值按照字段顺序 姓名、年龄、爱好
    print("\n\n\n", len(df))
    df.loc[len(df)] = ["诸葛亮", 55, "计谋"]
    print(df)
    # 方法二：通过索引的方式增加行，值根据字典指定
    df.loc[len(df)] = {"Name": "任小伟", "Age": 1024, "Gender": "学习"}
    print(df)
    # 方法三：通过pandas.concat([])拼接DataFrame
    df_a = pandas.concat([df, df], ignore_index=True)
    print(df_a)

    # 数据合并
    # merge(): 关联合并数据集
    # 参数
    #   left: 左侧的DataFrame，要进行合并的左侧数据集
    #     可选值: DataFrame
    #   right: 右侧的DataFrame，要进行合并的右侧数据集
    #     可选值: DataFrame
    #   how: 合并方式，指定如何对齐和合并数据
    #     可选值: left,right,inner,outer。默认值：inner
    #   on: 列名或列名列表，用于指定进行合并的列
    #     可选值: 列名或列名列表，如果要关联的名称两边都一样，可以直接用on
    #   left_on: 左侧DataFrame中用于合并的列
    #     可选值: 列名或列名列表，如果要关联的名称不一样，可以使用这个。支持列表参数
    #   right_on: 右侧DataFrame中用于合并的列
    #     可选值：列名或列名列表，如果要关联的名称不一样，可以使用这个。支持列表参数
    #   suffixes: 用于解决合并后列名冲突的后缀。
    #     可选值：原则或列表
    # 客户信息数据集
    customer_data = {
        "客户ID": ["001", "002", "003"],
        "姓名01": ["张三", "李四", "王五"],
        "年龄": [25, 30, 35]
    }
    df_customer = pandas.DataFrame(customer_data)
    print("\n\n", df_customer)

    # 订单信息数据集
    order_date = {
        "客户ID": ["001", "002", "003"],
        "姓名02": ["张三", "李四", "王五"],
        "订单号": ["A001", "A002", "A003"],
        "金额": [100, 200, 150]
    }
    df_order = pandas.DataFrame(order_date)
    print("\n\n", df_order)

    # 数据合并join
    df_merged_01 = pandas.merge(df_customer, df_order, on="客户ID")
    df_merged_02 = pandas.merge(left=df_customer, right=df_order, on="客户ID")
    df_merged_03 = pandas.merge(left=df_customer, right=df_order, left_on="客户ID", right_on="客户ID")
    df_merged_04 = pandas.merge(left=df_customer, right=df_order, left_on=["客户ID", "姓名01"], right_on=["客户ID", "姓名02"])
    df_merged_05 = pandas.merge(left=df_customer, right=df_order, how="inner", left_on=["客户ID"], right_on=["客户ID"])
    df_merged_06 = pandas.merge(left=df_customer, right=df_order, how="inner", left_on=["客户ID"], right_on=["客户ID"], suffixes=["_01", "_02"])
    print(df_merged_01)
    print(df_merged_02)
    print(df_merged_03)
    print(df_merged_04)
    print(df_merged_05)
    print(df_merged_06)

    #  concat(): union合并数据集
    df_a = pandas.concat([df_customer, df_customer], ignore_index=True)
    print(df_a)

    # 数据拆分
    # df[列名]: 获取指定列
    # loc[行索引1:行索引2, 列名]: 获取指定列，指定行。列名可以是list
    print(df_merged_06["客户ID"])
    print(df_merged_06.loc[1:3, ["客户ID", "姓名02", "年龄", "订单号", "金额"]])

    # 数据重塑与透视
    # 数据重塑：行转列(类似于平时做报表的时候，有很多金额列，可以转换成，有一列金额类型列，和一列金额列 )
    # melt(): 将宽格式的DataFrame转换为长格式，也称为"unpivot"操作
    # 参数：
    #   frame: 要进行转换的DataFrame
    #   id_vars: 保持不变的列，即转换后的长格式中的标识符列
    #   value_vars: 要转换的列，即转换后的长格式中的值列
    #   var_name: 用于标识值列的名称列的名称
    #   value_name: 用于标识值的列的名称
    sales_data = {
        "产品": ["A", "B"],
        "销售额1月": [1000, 2000],
        "销售额2月": [1500, 1800],
        "销售额3月": [1200, 2300]
    }
    df_sales = pandas.DataFrame(sales_data)
    print("\n\n", df_sales)
    # 数据重塑：行转列
    df_long_01 = pandas.melt(df_sales, id_vars=["产品"], value_vars=["销售额1月", "销售额2月", "销售额3月"], var_name="月份", value_name="销售额")
    df_long_02 = pandas.melt(df_sales, id_vars=["产品"], value_vars=["销售额1月", "销售额2月"], var_name="月份", value_name="销售额")
    print(df_long_01)
    print(df_long_02)

    # 数据透视
    #   数据透视是一种数据处理技术，用于将原始数据重新组织和汇总，以便更好地理解和分析数据的关系和趋势。
    #   透视表是数据透视的一种常见形式，它将数据按照指定的行和列进行分组，并对其中的数值进行聚合计算
    #   通过数据透视，可以根据自己的需求和分析目标，对数据进行灵活的重塑和汇总，以便从不同的角度和维度观察和理解数据
    # pivot: 数据透视
    # 参数：
    #   index: 维度(纵坐标)
    #   columns: 维度(横坐标)
    #   values: 指标(值)
    # pivot_table: 数据透视表
    #   类似pivot，pivot_table是一个通用的透视表函数，可以处理具有重复索引值的数据，并允许使用聚合函数对重复值进行汇总计算
    # 参数：
    #   data: 要进行透视表操作的数据集
    #   values: 用于聚合的列，即要进行透视和计算的值列
    #   index: 用于分组的列或列表，即透视表的行索引
    #   columns: 用于分组的列或列表，即透视表的列索引
    # 注意：
    #   pivot：不能处理重复值，维度和指标如果是重复的会报错
    #   pivot_table: 可以处理重复值，且可以对指标进行计算
    # groupby
    sales_data = {
        "产品": ["A", "A", "B", "B", "A", "B"],
        "月份": ["一月", "二月", "一月", "二月", "三月", "三月"],
        "销售额": [1000, 1500, 2000, 1800, 1200, 2300]
    }
    df_sales = pandas.DataFrame(sales_data)
    print("销售数据: \n", df_sales)
    print("数据透视: \n", df_sales.pivot(index="产品", columns="月份", values="销售额"))


    return


if __name__ == "__main__":
    # pandas基础
    # pandas_series()
    # pandas_dataframe()
    # pandas_dataframe_excel()

    # base_path = r"D:\02helloWorld\03Python\a01pythonLearn\excel"
    # pandas_excel_to_csv(base_path + "/table01.xlsx", base_path + "/table02.csv", skiprow=1, includeColums=["dt", "_col1"], excludeColums=["aa"])

    # pandas_dataframe_csv()

    # 数据查看
    # pandas_data_view()
    # pandas_corr()
    # pandas_handle_nan()

    # 数据清洗
    # 空字符&空字符串&缺失值处理
    # pandas_handle_nan_01()
    # 重复值处理
    # pandas_duplicate()
    # 异常值处理
    # pandas_handle_abnormal()
    # 数据类型转换
    # pandas_handle_type()
    # 数据格式化&规范化
    # pandas_handle_standard()

    # 数据预处理
    # 特征选择与删除
    pandas_handle_data()

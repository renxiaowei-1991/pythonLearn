#!/usr/bin/env python
# -*- coding:utf-8 -*-


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
    base_path = r"E:\07-python\07-projectList\a01PythonLearn\excel"
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
    base_path = r"E:\07-python\07-projectList\a01PythonLearn\excel"
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
    了解数据完整性
    isnull(): 检测数据中的缺失值。返回一个布尔型的DataFrame，标记了数据中的缺失值位置。对于缺失值位置，返回True，对于非缺失值位置，返回False
    notnull(): 检测数据中的非缺失值。返回一个布尔型的DataFrame，标记了数据中的非缺失值位置，对于非缺失值位置，返回True，对于缺失值位置，返回False
    isna(): isnull()的别名函数，执行相同的操作
    notna(): notnull()的别名函数，执行相同的操作
    any(): 检测DataFrame或Series对象中是否存在任何缺失值，返回一个布尔型值，如果存在缺失值，则为True，否则为False
    all(): 检测DataFrame或Series对象中的所有值是否都是缺失值，返回一个布尔值，如果所有值都是缺失值，则为True，否则为False
    
    sum(): 统计每列的数量，配合isnull() 可以统计每列缺失值数量

2.2、数据清洗
2.2.1、处理缺失值
    dropna(): 删除包含缺失值的行或列
    fillna(): 填充缺失值，选择适当的方法取决于具体的数据情况
2.2.2、处理重复值
    duplicated(): 检测重复值
    drop_duplicates(): 删除重复值，确保数据的唯一性
2.2.3、处理异常值
    通过使用可视化工具和基本统计分析来识别和处理异常值，可以使用过滤、替换或删除等方法来应对异常值
2.2.4、数据类型转换
    astype(): 将列的数据类型转换为正确的类型，确保数据的一致性和准确性
2.2.5、数据格式化与规范化
    对于字符串类型的数据，可以使用字符串处理函数，对数据进行格式化和规范化
    str.lower(): 转小写
    str.upper(): 转大写
    str.strip(): 去除空格

2.3、数据预处理
2.3.1、特征选择与删除
    根据分析目标和特征的相关性，选择相关特征并删除不相关或冗余的特征，以提高后续分析的效果。
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
    base_path = r"E:\07-python\07-projectList\a01PythonLearn\excel"
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

    # 缺失值检测
    base_path = r"E:\07-python\07-projectList\a01PythonLearn\excel"
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

    print(df_b[df_b["销售金额"]==" "])

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


if __name__ == "__main__":
    # pandas_series()
    # pandas_dataframe()
    # pandas_dataframe_excel()

    # base_path = r"E:\07-python\07-projectList\a01PythonLearn\excel"
    # pandas_excel_to_csv(base_path + "/table01.xlsx", base_path + "/table02.csv", skiprow=1, includeColums=["dt", "_col1"], excludeColums=["aa"])

    # pandas_dataframe_csv()
    pandas_data_view()
    # pandas_corr()
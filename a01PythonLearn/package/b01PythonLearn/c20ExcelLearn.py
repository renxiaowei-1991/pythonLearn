#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import xlrd
import xlwt
import xlutils3
from xlutils3.copy import copy

"""
Excel操作
    https://blog.csdn.net/m0_59235508/article/details/122808875

python能操作excel的库总共9个，对比如下：
                WIN MAX PY2 PY3 .xls    .xlsx   读   写   修改
    xlrd        是   是   是   是   是       是   是   否   否
    xlwt        是   是   是   是   是       否   否   是   是
    xlutils     是   是   是   是   是       否   否   否   是
    xlwings     是   是   是   是   是       是   是   是   是
    openpyxl    是   否   是   是   否       是   是   是   是
    xlswriter   是   是   是   是   否       是   否   是   否
    win32com    是   是   是   是   是       是   是   是   是
    DataNitro   是   否   是   是   是       是   平   平   平
    pandas      是   是   是   是   是       是   是   是   否

0、介绍
    Python操作excel主要用到xlrd和xlwt这两个库，xlrd是读excel，xlwt是写excel的库。
    xlrd库仅用于读取excel文件中的数据，xlwt库则用于将数据写入excel文件，但是对于已有的excel文件，想要追加或者修改，这两个库则没有办法完成。
    xlutils库也仅仅是通过复制一个副本进行操作后保存一个新文件，xlutils库就像是xlrd库和xlwt库之间的一座桥梁，因此，xlutils库是依赖于xlrd和xlwt两个库的。这三个库既能满足操作Excel的基本需求，
        xlutils进行复制和修改excel


1、xlrd
1.1、常用单元格的数据类型
    empty:空的
    string:text
    number
    date
    boolean
    error
    blank:空白表格

1.2、导入模块
    import xlrd

1.3、打开Excel文件读取数据
    data = xlrd.open_workbook(filename) #文件名以及路径，如果路径或者文件名有中文给前面加一个 r

1.4、常用函数
    excel中最重要的方法是boot和sheet的操作

3、xlutils
    安装xlutils的时候，如果报错，直接在终端使用pip安装
    pip install xlutils3
"""


def xlrdLearn():
    """
        excel读取练习
    :return:
    """
    # print(os.path.dirname(__file__))
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file\\a01PythonLearnFile\\excel"
    """
    注意：不能直接通过修改后缀来创建xls格式的文件。创建方式有两种
      1、先创建xlsx格式文件，再通过另存为，来存储为xls格式的文件
      2、按照支持创建xls格式excel软件，直接创建xls格式文件
    """
    fileName = "\\xlrdLearn.xls"
    # 打开文件
    data = xlrd.open_workbook(rootPath + fileName)

    # sheet操作
    print("sheet操作")
    # 1、通过索引顺序获取sheet，返回 xlrd.sheet.Sheet()对象
    table01 = data.sheets()[1]
    # 2、通过索引顺序获取sheet，返回 xlrd.sheet.Sheet()对象。
    # 注意：索引从1开始
    sheet_index = 1
    table02 = data.sheet_by_index(sheet_index)
    # 3、通过名称获取sheet，返回 xlrd.sheet.Sheet()对象
    sheet_name = 'test01'
    table03 = data.sheet_by_name(sheet_name)
    # 4、返回book中所有sheet的名字
    names = data.sheet_names()
    # 5、检查某个sheet是否导入完毕
    loadFlag = data.sheet_loaded(sheet_name or sheet_index)

    print("sheet列表：", names)
    print(sheet_name, " 是否导入完毕：", loadFlag)

    # 行操作
    print("行操作")
    # 1、获取sheet中的行数。注意：这里table.nrows后面不带().是属性
    nrows = table01.nrows
    # 2、返回指定行中所有单元格对象组成的列表。等价于 table.raw()
    rowx = 1
    rows01 = table01.row(rowx)
    # 3、返回指定行中所以单元格对象组成的列表
    rows02 = table01.row_slice(rowx)
    # 4、返回由该行中所以单元格的数据类型组成的列表。返回值为逻辑列表，若类型为empy则为0，否则为1
    rows03 = table01.row_types(rowx, start_colx=0, end_colx=None)
    # 5、返回由该行中所有单元格的数据组成的列表
    rows04 = table01.row_values(rowx, start_colx=0, end_colx=None)
    # 6、返回该行的有效单元格长度，即这一行有多少个数据
    leng = table01.row_len(rowx)

    print("sheet中的行数：", nrows)
    print(rowx + 1, "行的对象列表：", rows01)
    print(rowx + 1, "行的对象列表：", rows02)
    print(rowx + 1, "行的数据类型列表：", rows03)
    print(rowx + 1, "行的数据列表", rows04)
    print(rowx + 1, "行的有效单元格长度：", leng)

    # 列操作
    print("列操作")
    # 1、获取列表的有效列数
    ncols = table01.ncols
    # 2、返回由该列中所以的单元格对象组成的列表
    colx = 1
    cols01 = table01.col(colx, start_rowx=0, end_rowx=None)
    # 3、返回由该列中所有的单元格对象组成的列表
    cols02 = table01.col_slice(colx, start_rowx=0, end_rowx=None)
    # 4、返回由该列中所有单元格的数据类型组成的列表
    cols03 = table01.col_types(colx, start_rowx=0, end_rowx=None)
    # 5、返回由该列中所以单元格的数据组成的列表
    cols04 = table01.col_values(colx, start_rowx=0, end_rowx=None)

    print("sheet中的列数：", ncols)
    print(colx + 1, "列的对象列表：", cols01)
    print(colx + 1, "列的对象列表：", cols02)
    print(colx + 1, "列的数据类型列表：", cols02)
    print(colx + 1, "列的数据列表：", cols02)

    # 单元格操作
    print("单元格操作")
    # 1、返回单元格对象
    cell = table01.cell(rowx, colx)
    # 2、返回对象位置单元格中的数据类型
    type = table01.cell_type(rowx, colx)
    # 3、返回对象位置单元格中的数据
    value = table01.cell_value(rowx, colx)

    print(rowx, "行", colx, "列存储的对象：", cell)
    print(rowx, "行", colx, "列存储的数据类型：", type)
    print(rowx, "行", colx, "列存储的数据值：", value)


def xlwtLearn():
    """
        excel写入练习
        仅限xls格式
    :return:
    """

    # excel&sheet操作
    # 1、创建新的workbook(其实就是创建新的excel)
    workbook = xlwt.Workbook(encoding='ascii')
    # 2、创建新的sheet表
    sheet01 = workbook.add_sheet("test01")

    # 3、将数据写入sheet
    # 写入数据的格式控制
    type = 8
    # 通过格式控制标志，限定输出数据的格式
    if type == 1:
        # 1) 直接将数据不带格式的写入
        # 1、将数据写入表格
        sheet01.write(0, 0, "内容1")
        sheet01.write(2, 1, "内容2")
    elif type == 2:
        # 2) 设置字体格式
        # 1、初始化样式
        style = xlwt.XFStyle()
        # 2、为样式创建字体
        font = xlwt.Font()
        font.name = 'Times New Roman'  # 字体
        font.bold = True  # 加粗
        font.underline = True  # 下划线
        font.italic = True  # 斜体
        # 3、设置样式
        style.font = font
        # 4、将数据写入表格
        sheet01.write(0, 0, "内容1")
        sheet01.write(2, 1, "内容2", style)
    elif type == 3:
        # 3) 设置列宽
        """
        xlwt中列宽的值表示方法：默认字体0的1/256为衡量单位
        xlwt创建时使用的默认宽度为2960，即11个字符0的宽度
        所以设置列宽时可以用如下方法：
            width = 256 * 20 256为衡量单位，20表示20个字符宽度
        """
        # 1、将数据写入表格
        sheet01.write(0, 0, "内容1")
        sheet01.write(2, 1, "内容2")
        # 2、设置列宽
        sheet01.col(0).width = 256 * 20
    elif type == 4:
        # 4) 设置行高
        """
        在xlwt中没有特定的函数来设置默认的列宽及行高
        行高是在单元格的样式中设置的，可以通过自动换行通过输入文字的多少来确定行高
        """
        # 1、将数据写入表格
        sheet01.write(0, 0, "内容1")
        sheet01.write(2, 1, "内容2")
        # 2、设置行高
        style = xlwt.easyxf('font:height 360;')  # 18px,类型小初的字号
        sheet01.row(0).set_style(style)
    elif type == 5:
        # 5) 合并列和行
        # 1、将数据写入表格
        sheet01.write(0, 0, "内容1")
        # 2、合并 第1行到第2行 的 第0列到第3列
        # 第一行已经写入，不可合并
        # sheet01.write_merge(0, 1, 0, 2, "Merge Test")
        sheet01.write_merge(1, 2, 0, 2, "Merge Test")
    elif type == 6:
        # 6) 边框
        # 1、设置边框样式
        borders = xlwt.Borders()  # Create Borders
        """
        May be:
            NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR,
            MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
            MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        DASHED 虚线
        NO_LINE 没有
        THIN 实线
        """
        borders.left = xlwt.Borders.DASHED  # 左边框
        borders.right = xlwt.Borders.DASHED  # 右边框
        borders.top = xlwt.Borders.DASHED  # 上边框
        borders.bottom = xlwt.Borders.DASHED  # 下边框
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40

        style = xlwt.XFStyle()  # Create Style
        style.borders = borders  # Add Borders to Style
        # 2、将数据写入表格
        sheet01.write(0, 0, "内容1")
        sheet01.write(2, 1, "内容2", style)
    elif type == 7:
        # 7) 为单元格设置背景色
        # 1、将数据写入表格
        sheet01.write(0, 0, "内容1")
        # 2、创建样式
        pattern = xlwt.Pattern()
        """
        May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        """
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        """
        # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow,
        # 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow ,
        # almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
        """
        pattern.pattern_fore_colout = 5
        style = xlwt.XFStyle()
        style.pattern = pattern
        # 3、使用样式将数据写入表格
        sheet01.write(2, 1, "内容2", style)
    elif type == 8:
        # 8) 设置单元格对齐
        """
        使用xlwt中的Alignment来设置单元格的对齐方式，其中horz代表水平对齐方式，vert代表垂直对齐方式。
        VERT_TOP = 0x00 上端对齐
        VERT_CENTER = 0x01 居中对齐（垂直方向上）
        VERT_BOTTOM = 0x02 低端对齐
        HORZ_LEFT = 0x01 左端对齐
        HORZ_CENTER = 0x02 居中对齐（水平方向上）
        HORZ_RIGHT = 0x03 右端对齐
        """
        # 1、将数据写入表格
        sheet01.write(0, 0, "内容1")
        # 2、创建样式
        al = xlwt.Alignment()
        al.horz = 0x02  # 设置水平居中
        al.vert = 0x01  # 设置垂直居中
        style = xlwt.XFStyle()
        style.alignment = al
        # 3、使用样式将数据写入表格
        sheet01.write(2, 1, "内容2", style)

    # 4、保存
    # print(os.path.dirname(__file__))
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn\\file\\a01PythonLearnFile\\excel"
    fileName = "\\xlwtLearn.xls"
    # 保存的时候是保存workbook，而不是sheet01
    # 保存就是将已经建立好的对象，存储到文件系统中
    workbook.save(rootPath + fileName)


def xlutilsCopyLearn():
    """
    excel复制练习
    :return:
    """
    """
    1、打开工作簿(其实就是把excel创建为对象)
    默认formatting_info=False ，不保留格式
    formatting_info=True，保留格式，但是会报错。需要查看原因
    """
    # print(os.path.dirname(__file__))
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn"
    subPath = "\\file\\a01PythonLearnFile\\excel\\"
    inFileName = "xlrdLearn.xls"
    # workBook = xlrd.open_workbook(rootPath + subPath + inFileName, formatting_info=True)
    workBook = xlrd.open_workbook(rootPath + subPath + inFileName)

    # 2、将xlrd对象拷贝转化为xlwt对象
    """
    1、xlutils3.copy(workBook) 会报错
    2、xlutils3.copy.copy(workBook) 会报错
    3、先导入，再使用不会报错
        from xlutils3.copy import copy
        copy(workBook)
    4、复制的表格，样式会全部消失
    """
    # newWorkBook = xlutils3.copy(workBook)
    # newWorkBook = xlutils3.copy.copy(workBook)
    newWorkBook = copy(workBook)

    # 3、保存工作簿
    outFileName = "xlutilsLearn.xls"
    newWorkBook.save(rootPath + subPath + outFileName)


def xlutilsUpdateLearn():
    """
    excel变更练习
    :return:
    """
    # 1、打开工作簿(其实就是把excel创建为对象)
    # print(os.path.dirname(__file__))
    rootPath = "E:\\07-python\\07-projectList\\a01PythonLearn"
    subPath = "\\file\\a01PythonLearnFile\\excel\\"
    inFileName = "xlrdLearn.xls"
    workBook = xlrd.open_workbook(rootPath + subPath + inFileName)

    # 2、将xlrd对象拷贝转化为xlwt对象
    """
    1、xlutils3.copy(workBook) 会报错
    2、xlutils3.copy.copy(workBook) 会报错
    3、先导入，再使用不会报错
        from xlutils3.copy import copy
        copy(workBook)
    4、复制的表格，样式会全部消失
    """
    # newWorkBook = xlutils3.copy(workBook)
    # newWorkBook = xlutils3.copy.copy(workBook)
    newWorkBook = copy(workBook)

    # 3、读取表格信息
    sheet = workBook.sheet_by_index(0)
    col2 = sheet.col_values(1)  # 取出第二列
    cel_value = sheet.cell_value(1, 1)
    print(col2)
    print(cel_value)

    # 4、写入表格信息
    write_save = newWorkBook.get_sheet(0)
    write_save.write(0, 0, "xlutils写入!")

    """
    5、保存工作簿
    保存的时候直接将workBook保存到输入文件中，就是修改文件的操作
    """
    outFileName = "xlutilsLearn.xls"
    newWorkBook.save(rootPath + subPath + outFileName)
    # 报错到输入文件中，就是修改文件的操作
    # newWorkBook.save(rootPath + subPath + inFileName)


if __name__ == '__main__':
    # xlrdLearn()   #读excel
    # xlwtLearn()   #写excel
    # xlutilsCopyLearn() #改excel
    xlutilsUpdateLearn()
    
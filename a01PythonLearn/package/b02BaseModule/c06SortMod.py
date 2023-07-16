#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SortClass:
    """
    自己开发的各种排序方法。练习使用
    """
    sort_type = "default"

    def __init__(self):
        pass

    @classmethod
    def upSort(self, list_in):
        """
        升序排序
        :return:
        """
        list_a = list_in
        if SortClass.sort_type == "default":
            SortClass().defaultSort(list_a)
        elif SortClass.sort_type == "bubbling":
            SortClass().bubblingSort(list_a)
        else:
            SortClass().defaultSort(list_a)
        return True

    @classmethod
    def downSort(self, list_in):
        """
        降序排序
        :return:
        """
        list_a = list_in
        SortClass.upSort(list_a)
        list.sort(list_a, reverse=True)
        return True

    def bubblingSort(self, list_in:list):
        """
        冒泡排序
        :return:
        """
        list_a = list_in
        for i in range(len(list_a) - 1):
            print(f"第{i}轮")
            for j in range(len(list_a) - i - 1):
                num = 0
                if list_a[j] >= list_a[j + 1]:
                    num = list_a[j]
                    list_a[j] = list_a[j + 1]
                    list_a[j + 1] = num
                print("i=", i, ",j=", j)
                print(list_a)
        return True


    def sinkSort(self):
        """
        下沉排序
        :return:
        """
        pass

    def dichotomySort(self):
        """
        二分法排序
        :return:
        """
        pass

    def defaultSort(self, list_in: list):
        """
        使用默认排序
        :param list_in:
        :return:
        """
        list_in.sort()
        return True


def SortClass_test():
    """排序测试"""
    # lista = list(range(1, 100, 3))
    # SortClass.downSort(lista)
    lista = [3, 6, 23, 1, 55, 22]
    SortClass().bubblingSort(lista)
    print(lista)


# SortClass_test()

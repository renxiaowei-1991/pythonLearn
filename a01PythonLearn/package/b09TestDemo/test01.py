#!/usr/bin/env python
# -*- coding=utf-8 -*-
import math


class numClass:
    def __init__(self):
        self.dataList = []
        self.sortDataList = []


    def addNum(self, num):
        self.dataList.append(num)
        print(None)
        return None


    def sortSelf(self):
        self.sortDataList = self.dataList

        for i in range(len(self.dataList) - 1):
            print("i=", i)
            var = 0
            for j in range(i, len(self.dataList) - 1, 1):
                print("j=",j)
                if(self.dataList[i] <= var):
                    var = self.dataList[i]
            self.sortDataList[i] = var
        return


    def findMedian(self):
        self.sortSelf()
        print(self.dataList)
        print(self.sortDataList)
        result = 0
        if(len(self.sortDataList) % 2 == 1):
            num = math.floor(len(self.sortDataList) / 2)
            print("num=", num)
            result = self.sortDataList[num]
        else:
            num1 = math.floor(len(self.sortDataList) / 2) - 1
            num2 = math.ceil(len(self.sortDataList) / 2)
            print("num1=", num1)
            print("num2=", num2)
            result = (self.sortDataList[num1] + self.sortDataList[num2]) / 2

        print(result)
        return result


if __name__ == "__main__":
    num_class = numClass()
    num_class.addNum(10)
    num_class.addNum(6)
    num_class.findMedian()
    num_class.addNum(7)
    num_class.addNum(8)
    num_class.addNum(9)
    num_class.findMedian()
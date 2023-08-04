#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
    条件语句
        python不支持switch语句
        可以将语句写到同一行

        if 判断条件1:
            执行语句1...
        elif 判断条件2:
            执行语句2...
        elif 判断条件3:
            执行语句3...
        else:
            执行语句4...

"""
print("条件语句练习")
flag = False
name = 'luren'
if name == 'python':
    flag = True
    print("welcome boss")
else:
    print(name)

num = 5
if num == 3:
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:
    print('error')
else:
    print('roadman')

var = 100
if (var == 100): print("变量var的值为100")

"""
    循环语句

    while循环
        while 判断条件(condition):
            执行语句(statements)...
        else:
            执行语句(statements)

        判断条件可以是任何表达式、任何非零、非空(null)的值均为true
        循环条件为false时执行else

        while 判断条件(condition): 执行语句(statements)...

    for循环
        for iterating_var in sequence:
            statements(s)

        for iterating_var in sequence:
            statements(s)
        else:
            statements(s)

        for循环可以遍历任何序列的项目，如列表、字符串
        else 在循环正常执行完的情况下执行。(通过break跳出的不执行)
        len() 返回列表的长度，即元素的格式
        range() 返回一个序列的数

    嵌套循环
        for iterating_var in sequence:
            for iterating_var in sequence:
                statements(s)
            statements(s)

        while expression:
            while expression:
                statements(s)
            statements(s)

    循环控制语句
    break 跳出循环
        break 语句用来停止循环语句
        break 语句停止嵌套循环中的break语句所在层次循环

    continue 跳过该次循环，执行下一次循环
        continue 语句用来跳过当前循环剩余语句，继续进行下一轮循环
        conitnue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分

    pass 占位符，空语句
        pass 是空语句，是为了保持结构的完整性
        pass 不做任何事情，一般用作占位语句

"""
print("while循环练习：")
a = 1
while a < 10:
    a += 1
    if a == 5: continue
    if a == 7: break
    print(a)
else:
    print(100)

print("for循环练习：")
print("for循环练习：字符串")
for letter in 'python':
    print("当前字母：%s" % letter)

print("for循环练习：列表")
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print(fruit)

print("for循环练习：索引")
for index in range(len(fruits)):
    print(fruits[index])

print("for循环练习：找质数")
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d 等于 %d * %d' % (num, i, j))
            break
    else:
        print('%d 是一个质数' % num)

print("嵌套循环练习：while嵌套(找质数)")
i = 3
num = 0
primeNumList = []
while i <= 100:
    j = 2
    while j < i:
        if (i % j == 0):
            num = i / j
            print("%d 等于 %d 乘 %d" % (i, j, num))
            break
        j += 1
    else:
        print("%d 是质数" % i)
        primeNumList.append(i)
    i += 1
print("2~100的质数列表：", primeNumList)

print("break练习")
for i in range(10):
    for j in range(5):
        if i == 5:
            break
        print(i, j)

print("continue练习")
for letter in 'python':
    if letter == 't':
        continue
    print(letter)

# if判断
num = int(input())
if num < 60:
    print("E")
elif (num >= 60) and (num < 70):
    print("D")
elif (num >= 70) and (num < 80):
    print("C")
elif (num >= 80) and (num < 90):
    print("B")
elif (num >= 90) and (num < 100):
    print("A")
else:
    print("S")

# while循环
inputArray = input().split(",")
startNum = int(inputArray[0])
endNum = int(inputArray[1])
print("startNum", startNum)
print("endNum", endNum)
numSum = 1
while startNum <= endNum:
    numSum *= startNum
    startNum += 1
else:
    print("求和结束，总数是：", numSum)

# for循环
arrayList = [12, 34, 56, 78]
arrayTuple = (12, 34, 56, 78)
stringA = "abcdefghijklmnopqrstuvwxyz"
for strA in arrayList:
    print(strA)
for strA in arrayTuple:
    print(strA)
for strA in stringA:
    print(strA)
for num in range(10):
    print(num)

for i in range(10):
    print("i:", i)
    for j in range(20):
        if j in [5, 15]:
            continue
        print("j:", j)
        if j == 18:
            break
            
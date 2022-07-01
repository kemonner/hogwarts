# 1.format使用
# a = 'aaa'
# b = 'bbb'
# c = 'ccc{x}{y}'
# print(c.format(x=a, y=b))
# 2.列表浮标
# list1 = [1, 2, 3, 4, 5, 6]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[-1])
# 3.切片的使用
# print(list1[0:3])
# 4.计算1-100求和
# a = 0
# for i in range(101):
#     a = a+i
# print(a)
# 5.实现1-100之间偶数求和
# a = 0
# for i in range(101):
#     if i % 2 == 0:
#         a = a+i
# print(a)
# a = 0
# for i in range(2, 101, 2):
#     a = a+i
# print(a)
"""
6.break和continue
break语句可以跳出for和while循环体。如果你从for或while循环中终止，任何对应的循环else块将不执行
continue语句被用来告诉python跳过当前循环快中的剩余语句，然后继续进行下一轮循环。
"""
# for i in range(1,10):
#     print(i)
#     if i == 6:
#         break
# for i in range(1, 10):
#     if i == 6:
#         continue
#     print(i)
# 7.python实现1-100之间偶数求和
# a = 1
# while a == 1:
#     print("a=1")
#     a = a + 1
# else:
#     print("a!=1")
"""
8.计算机随机出一个1-100之间的数由人来猜，计算机根据人猜的数字分别给出提示：猜大了/猜小了/猜对啦
"""
# import random
# human_number = 0
# com_number = random.randint(1, 100)
# while True:
#     human_number = int(input("请输入你猜测的数字："))
#     if human_number > com_number:
#         print("猜大了")
#     elif human_number < com_number:
#         print("猜小了")
#     elif human_number == com_number:
#         print("猜对了")
"""
9.return
"""
# def method(a):
#     print(a)
#     return a+2
# print(method(1))

# def method(a, b=[]):
#     b.append(a)
#     return b
# print(method(1))
# print(method(2))
"""
10.参数传递字典(打印key值)
**a表示定义字典传参
"""
# def method(**q):
#     print(q.keys())
# method(a=1, b=2, c=3)
"""
11.元组传参
*a形参定义的是一个元祖
"""
# def method(*a):
#     print(a[1])
#     print(a[2])
#     print(a[3])
#     print(a[4])
# method(1,2,3,4,5)
"""
12.(1)如何生成一个平方列表 (2)使用列表推导式该如何生成 (3)如何生成一个平方列表，不要某些数字的 (4)将(3)用列表推导式写出
"""
# (1)
# list_square = []
# for i in range(1,4):
#     list_square.append(i**2)
# print(list_square)
# (2)
# list_square = [i**2 for i in range(1, 4)]
# print("list_square=", list_square)
# (3)
# list_square = []
# for i in range(1, 4):
#     if i != 1:
#         list_square.append(i**2)
# print(list_square)
# (4)
# list_square =[i**2 for i in range(1, 4) if i != 1]
# print("list_square=", list_square)
"""
13.(1)嵌套循环 【1, 2, 3, 2, 4, 6, 3, 6, 9】(2)使用列表推导式嵌套循环 (3)字典推导式
"""
# (1)
# list_multiply = []
# for i in range(1, 4):
#     # 执行到这里的时候，要把第二个for循环全部乘一遍
#     for q in range(1, 4):
#         list_multiply.append(i*q)
# print(list_multiply)
# (2)
# list_multiply = [i*q for i in range(1, 4) for q in range(1, 4)]
# print("list_multiply", list_multiply)
# (3)
# dict_list = [{i: i**2 for i in range(1,4)}]
# print(dict_list)
"""
14.打印当前执行文件的绝对路径
"""
# import sys
# print("调用sys")
# for i in sys.argv:
#     print(i)
"""
15.字面量插值
"""
# name = 'tom'
# name1 = 'jerry'
# name2 = ['tom1', 'jerry2']
# name3 = {'name': 'tom2', 'age': 19}
# print('my name is {}, his name is {}'.format(name, name1))
# print('my name is {0}, his name is {1}'.format(*name2))
# print('my name is {name}, my age is {age}'.format(**name3))
"""
16.异常处理
"""
# num1 = int(input("请输入一个除数："))
# num2 = int(input("请输入被除数："))
# print(num1/num2)
# try:
#     num1 = int(input("请输入一个除数："))
#     num2 = int(input("请输入被除数："))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("被除数不能为0")
# except ValueError:
#     print("被除数需要是数值型整数")
# else:
#     print("没有异常时执行的代码")
# finally:
#     print("无论是否发生异常，都执行")

# 主动抛出异常
# x = 10
# if x > 5:
#     raise Exception("这是主动抛出的异常信息")

# 自定义异常
# class Myexception(Exception):
#     def __init__(self, value1, value2):
#         self.value1 = value1
#         self.value2 = value1
# raise Myexception("value1", "value2")
"""
17.python常用标准库 操作系统相关：os
"""
# import os
# os.mkdir("osmkdir")
# print(os.listdir("./"))
# os.removedirs("osmkdir")
# print(os.getcwd())
# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt", "w")
#     f.write("hellp, os using")
"""
18.python常用标准库 时间与日期相关：time datetime
"""
import time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y年%m月%d日 %H:%M:%S秒", time.localtime()))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print(time.strftime("%Y:%m:%d %H:%M:%S", time.localtime()))
# 获取两天前的时间
# nowtime = time.time()
# two_days_before = nowtime - 60*60*24*2
# time_tuple = time.localtime(two_days_before)
# print(time.strftime("%Y年%m月%d日 %H:%M:%S秒", time_tuple))
"""
19.python常用标准库 网络请求相关：urllib
"""
# import urllib.request
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# # print(response.headers)
# print(response.read())
"""
20.python常用标准库 科学计算相关：math
"""
# import math
# 返回大于等于参数x的最小整数 ceil(x)
# print(math.ceil(5.5))
# 返回小于等于参数x的最大整数 floor(x)
# print(math.floor(4.999))
# 平方根 sqrt(x)
# print(math.sqrt(9))
"""
21.range函数自动生成什么
"""
# loops = [2, 4]
# ra = range(len(loops))
# print(ra)
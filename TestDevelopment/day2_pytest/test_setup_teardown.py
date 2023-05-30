# -*- coding:utf-8 -*-
"""
   模块级(setup_module/teardown_module)模块始末，全局的（优先级最高）
   函数级(setup_function/teardown_function)只对函数用例生效（函数不在类中）
   方法级(setup_method/teardown_method)开始于方法始末（方法在类中）
   类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
   类里面的(setup/teardown)运行在调用方法前后
"""


# 模块级别,只调用一次
def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源清理：teardown module")


# function函数级别的，不在类中，只对函数生效
def test_case1():
    print("case1")


def test_case2():
    print("case2")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源清理：teardown function")


class TestDemo:

    # 执行类 前后分别执行setup_class teardown_class,分别被调用一次
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类的方法前后分别执行setup,teardown
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def setup_method(self):
        print("test_demo setup_method")

    def teardown_method(self):
        print("test_demo teardown_method")

    def test_demo1(self):
        print("test test_demo1")

    def test_demo2(self):
        print("test test_demo2")


class TestDemo1:

    # 执行类 前后分别执行setup_class teardown_class,分别被调用一次
    def setup_class(self):
        print("TestDemo setup_class1")

    def teardown_class(self):
        print("TestDemo teardown_class1")

    # 每个类的方法前后分别执行setup,teardown
    def setup(self):
        print("TestDemo setup1")

    def teardown(self):
        print("TestDemo teardown1")

    def test_demo3(self):
        print("test demo3")

    def test_demo4(self):
        print("test demo4")
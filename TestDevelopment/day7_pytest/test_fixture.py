"""
    场景：
        测试⽤例执⾏时，有的⽤例需要登陆才能执⾏，有些⽤例不需要登陆。
        setup 和 teardown ⽆法满⾜。fixture 可以。默认 scope（范围）function
    步骤：
        1.导⼊ pytest
        2.在登陆的函数上⾯加@pytest.fixture()
        3.在要使⽤的测试⽅法中传⼊（登陆函数名称），就先登陆
        4.不传⼊的就不登陆直接执⾏测试⽅法。
"""
import pytest


# 登录
# 在登陆的函数上⾯加@pytest.fixture()
@pytest.fixture(scope="module")
def login():
    print("完成登录操作")

# 传⼊的是不需要登陆直接就可以执⾏的测试方法
def test_02(login):
    print("搜索")

# 需要先登录才能测试的测试方法中传⼊（登陆函数名称），先登陆，在运行测试
def test_03(login):
    print("加入购物车")

# # 需要先登录才能测试的测试方法中传⼊（登陆函数名称），先登陆，在运行测试
def test_04(login):
    print("下单")

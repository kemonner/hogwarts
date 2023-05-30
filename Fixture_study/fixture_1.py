# fixture的使用范围，如果没有定义fixture的scope作用域，那么不管这个fisture定义在哪里，哪怕是在不同的类内，也可以请求它。
# 夹具可用性是从测试的角度确定的。只有在定义夹具的范围内，夹具才可供测试请求。如果夹具定义在类内，则只能由该类内的测试请求，
# 但是如果在模块的全局范围内定义了一个fixture，那么该模块中的每个测试，即使它是在一个类中定义的，都可以请求它。
# import pytest
#
#
# @pytest.fixture
# def order():
#     return []
#
#
# @pytest.fixture
# # order:[]
# def outer(order, inner):   # order:["outer"]
#     order.append("outer")
#     print('1', order)  # 第二个输出：('1',['one', 'outer'])
#
#
# class TestOne:
#     @pytest.fixture
#     def inner(self, order):
#         # order:[]
#         print('2', order)  # 第一个输出：('2', [])
#         order.append("one")  # order:['one']
#
#     # 从这里开始
#     def test_order(self, order, outer):
#         print('3', order)
#         assert order == ["one", "outer"]
#
#
# class TestTwo:
#     @pytest.fixture
#     def inner(self, order):
#         order.append("two")
#         print('4', order)
#
#     def test_order(self, order, outer):
#         assert order == ["two", "outer"]
#         print('5', order)

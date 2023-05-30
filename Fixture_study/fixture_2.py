# order 层级最高，其他都是依赖于order，虽然order和sess作用域scope都是session，但是sess依赖了order
# 优先级分别是：session>package>module>class>function
# 测试将通过，因为较大范围的固定装置首先执行，而class TestClass未定义范围所以最后执行。
# import pytest
#
#
# @pytest.fixture(scope="session")
# def order():
#     print(1, '[]')
#     return []
#
#
# @pytest.fixture
# def func(order):
#     order.append("function")
#     print(2, order)
#
#
# @pytest.fixture(scope="class")
# def cls(order):
#     order.append("class")
#     print(3, order)
#
#
# @pytest.fixture(scope="module")
# def mod(order):
#     order.append("module")
#     print(4, order)
#
#
# @pytest.fixture(scope="package")
# def pack(order):
#     order.append("package")
#     print(5, order)
#
#
# @pytest.fixture(scope="session")
# def sess(order):
#     order.append("session")
#     print(6, order)
#
#
# # 测试将通过，因为较大范围的固定装置首先执行，而class TestClass未定义范围所以最后执行。
# class TestClass:
#     def test_order(self, func, cls, mod, pack, sess, order):
#         assert order == ["session", "package", "module", "class", "function"]

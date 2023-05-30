# 基于依赖关系执行相同顺序的夹具
# import pytest


# @pytest.fixture
# def order():     # []
#     return []


# @pytest.fixture
# def a(order):   # ["a"]
#     print(1, order)
#     order.append("a")
#     print(2, order)
#
#
# @pytest.fixture
# def b(a, order):    # ["a","b"]
#     print(3, order)
#     order.append("b")
#     print(4, order)
#
#
# @pytest.fixture
# def c(a, b, order):  # ["a","b","c"]
#     print(5, order)
#     order.append("c")
#     print(6, order)   # 6, ["a","b","c"]
#
#
# @pytest.fixture
# def d(c, b, order):
#     print(7, order)
#     order.append("d")
#     print(8, order)
#
#
# @pytest.fixture
# def e(d, b, order):
#     print(9, order)
#     order.append("e")
#     print(10, order)
#
#
# @pytest.fixture
# def f(e, order):
#     print(11, order)
#     order.append("f")
#     print(12, order)
#
#
# @pytest.fixture
# def g(f, c, order):
#     print(13, order)
#     order.append("g")
#     print(14, order)


# def test_order(g, order):
#     assert order == ["a", "b", "c", "d", "e", "f", "g"]

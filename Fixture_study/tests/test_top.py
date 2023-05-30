# conftest.py: 跨多个文件共享夹具
# content of tests/test_top.py
import pytest


# 执行顺序：先调用order再调用innermost
@pytest.fixture
def innermost(order):
    order.append("innermost top")
    print(1, order)


# 再调用top 最后调用test_order
def test_order(order, top):
    print(2, order)
    assert order == ["innermost top", "top"]

# 顺序：order innermost top test_order
# 结果：'s','top' order:["innermost top"]   1, ["innermost top"]  3, ["innermost top",'top']  2 ["innermost top",'top']

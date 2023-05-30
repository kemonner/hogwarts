import pytest


# 参数化的名字，要与方法中的参数名一一对应。
# 如果传递多个参数的话，要放在列表中，列表嵌套列表或者元组
# ids重命名，ids的个数要 == 传递的数据的个数
@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("4+2", 6), ("7+8", 15)],
                         ids=["number1", "number2", "number3"])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected

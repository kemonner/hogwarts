import pytest


@pytest.mark.xfail
def test_case1():
    print("test_xfail执行")
    assert 1 == 1


fail = pytest.mark.xfail


@fail(reason='bug 110')
def test_case2():
    assert False


def test_case3():
    print("***开始测试***")
    pytest.xfail(reason="该功能尚未完成")
    print("***测试过程***")
    assert 1 == 2



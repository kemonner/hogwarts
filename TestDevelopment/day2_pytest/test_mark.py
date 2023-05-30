import pytest


def double(a):
    return a * 2

# Pytest标记测试用例
# 测试数据类型：整形
@pytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)


# 测试数据类型：复数
@pytest.mark.minus
def test_double_minus():
    print("test double minus")
    assert -2 == double(-1)


# 测试数据类型：浮点数
@pytest.mark.float
def test_double_float():
    print("test double float")
    assert 0.2 == double(0.1)


@pytest.mark.float
def test_double_float():
    print("test double float")
    assert -10.2 == double(-0.1)


@pytest.mark.zero
def test_double_0():
    print("test double 0")
    assert 10 == double(0)


@pytest.mark.bignum
def test_double_bignum():
    print("test bignum")
    assert 200 == double(100)


@pytest.mark.str
def test_double_str1():
    print("test double str1")
    assert 'aa' == double('a')


@pytest.mark.str
def test_double_str2():
    print("test double str2")
    assert 'a$a$' == double('a$')

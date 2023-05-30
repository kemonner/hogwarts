import pytest


def double(a):
    return a*2


# 测试数据，整型
@pytest.mark.int
def test_double_int():
    print('test double int')
    assert 6 == double(3)


@pytest.mark.minus
def test_double_minus1():
    print('test double minus')
    assert -2 == double(-1)


@pytest.mark.float
def test_double_float():
    assert 6.2 == double(3.1)


@pytest.mark.minus
def test_double_minus2():
    print('test double minus')
    assert -0.2 == double(-0.1)


@pytest.mark.zero
def test_double_0():
    assert 0 == double(0)


@pytest.mark.bignum
def test_double_bignum():
    assert 7998 == double(3999)


@pytest.mark.bignum
def test_double_bignum():
    assert 7998 == double(3999)


@pytest.mark.str
def test_double_str():
    assert 'strstr' == double('str')


@pytest.mark.str
def test_double_str1():
    assert 'strstr' == double('str')


# if __name__ == "__main__":
#     # 1.运行当前目录下所有符合规则的用例，包括子目录(test_*.py 和 *_test.py)
#     # pytest.main()相当于pytest.main('./')执行当前目录下所有
#     # pytest.main()
#     # 2.运行test_mark1.py::test_dkrj模块儿中的某一条用例
#     # pytest.main(['test_param.py::test_te1', '-vs'])
#     # 3.运行某个标签
#     pytest.main(['test_commond_param.py', '-vs', '-m', 'str'])

import pytest
import itertools


def test_te1():
    aa = itertools.product(['西藏','瀑布','湖水'], ['月色','星空'])
    bb = list(aa)   #按照顺序生成笛卡尔积，repeat默认是1
    print(bb)


def test_demo1():
    assert 2*2 == 4


def test_demo2():
    assert 9/3 == 3


numbers = [1, 2, 3]
vowels = ['+', '-', '*']
consonants = ["x", "y", "z"]


cartesian = [elem for elem in itertools.product(*['numbers', 'vowels', 'consonants'])]


@pytest.fixture(params=cartesian)
def someparams(request):
    return request.param


def test_somthing(someparams):
    pass
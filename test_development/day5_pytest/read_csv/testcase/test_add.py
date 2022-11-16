import pytest
from test_development.day5_pytest.read_csv.func.operation import my_add
import csv


def test_get_csv1():
    with open(r"/Users/zxmac/Desktop/workspace/project/hogwarts/test_development/day5_pytest/read_csv/data/params.csv") \
            as file:
        raw = csv.reader(file)
        print(type(raw), raw, "aaaaa")
        list1 = []
        for line in raw:
            print(type(line), line, "bbbbb")
            list1.append(line)
        print(type(list1), list1, "ccccc")
        return list1

def test_get_csv2():
    with open(r"/Users/zxmac/Desktop/workspace/project/hogwarts/test_development/day5_pytest/read_csv/data/params1.csv") \
            as file:
        raw = csv.reader(file)
        print(type(raw), raw, "aaaaa")
        list1 = []
        for line in raw:
            print(type(line), line, "bbbbb")
            list1.append(line)
        print(type(list1), list1, "ccccc")
        return list1


class TestWithCsv:
    @pytest.mark.parametrize("x, y, expect", test_get_csv1())
    def test_csv1(self, x, y, expect):
        assert my_add(x, y) in ("Linux从入门到高级linux", "web自动化测试进阶python", "app自动化测试进阶python",
                                "Docker容器化技术linux", "测试平台开发与实战python")

    @pytest.mark.parametrize("x, y, expect", test_get_csv2())
    def test_csv2(self, x, y, expect):
        assert my_add(int(x), int(y)) == int(expect)

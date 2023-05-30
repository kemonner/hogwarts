import pytest
from TestDevelopment.day5_pytest.read_json.func.operation import my_add
import json


def test_get_json():
    with open("/TestDevelopment/day5_pytest/read_json/data/"
              "params1.json") as file:
        # 将json文件解析为一个字典
        data1 = json.loads(file.read())
        print(type(data1), data1, "11111")
        # 接收一个字典对象，并将它转换成一个文本格式的json的一个对象
        data2 = json.dumps(data1, ensure_ascii=False)
        print(type(data2), data2, "22222")

    # 获取数据内容
    with open("/TestDevelopment/day5_pytest/read_json/data/"
              "params.json", "r") as f:
        # 将json格式的文件转换为一个字典对象
        data = json.loads(f.read())
        print(type(data), data, "aaaaa")
        # 将字典中的值取出
        data1 = data.values()
        print(type(data1), data1, "bbbbb")
        list1 = []
        # 将字典中的值遍历放入列表中
        for da in data1:
            list1.append(da)
            print(type(da), da, "ccccc")
        print(type(list1), list1, "ddddd")
        return list1


class TestWithJson:
    @pytest.mark.parametrize("x, y, excepted", test_get_json())
    def test_add(self, x, y, excepted):
        assert int(x) + int(y) == int(excepted)




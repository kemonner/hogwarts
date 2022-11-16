"""
思想：
    yml文件包括测试数据data，步骤step，读取测试步骤，获得计算方法，数据也从yml文件中获取。
详细步骤：
    需要使用某一方法的时候，通过获取steps.yml中的步骤方法名，导出成一个列表，遍历这个列表找到需要使用的方法，然后通过导包获取calc方法，
    判断当遍历的这个方法名和calc中方法名相同时，就使用这个方法，数据也从yml文件中获取,通过yaml.safe_load方法获取的数据是列表格式
"""
import pytest
import yaml

from calc import Calc


def get_steps():
    with open('/Users/zxmac/Desktop/workspace/project/hogwarts/datas/steps.yml') as f:
        return yaml.safe_load(f)


class Test_pytest:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('data1, data2, expect', yaml.safe_load(open('/Users/zxmac/Desktop/workspace/project/hogwar'
                                                                         'ts/datas/sub.yml')))
    def test_sub_1(self, data1, data2, expect):
        print(data1, data2, expect)
        steps = get_steps()
        for step in steps:
            if step == 'sub':
                result = self.calc.sub(data1, data2)
                print(result)
                assert expect == result


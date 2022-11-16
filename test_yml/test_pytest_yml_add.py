import pytest
import yaml

from calc import Calc
from decimal import Decimal


def steps():
    with open('/Users/zxmac/Desktop/workspace/project/hogwarts/datas/steps.yml') as f:
        return yaml.safe_load(f)


class Test_pytest:
    def setup(self):
        self.calc = Calc()

    def test_add(self):
        # self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        print(type(result))
        assert 3 == result

    @pytest.mark.parametrize('data1, data2, expect', yaml.safe_load(open('/Users/zxmac/Desktop/workspace/project'
                                                                         '/hogwarts/datas/add1.yml')))
    def test_add_1(self, data1, data2, expect):
        # self.calc = Calc()
        step1 = steps()
        for step in step1:
            print(f'step === > {step}')
            if 'add' == step:
                result = self.calc.add(data1, data2)
                print(result)
                print(data1, data2, expect)
                assert expect == result
            elif 'add1' == step:
                result = self.calc.add1(data1, data2)
                print(result)
                print(data1, data2, expect)
                print(2)
                assert expect == result


        # result = self.calc.add(data1, data2)
        # print(result)
        # assert expect == result
        #
        # result1 = self.calc.add1(data1, data2)
        # print(result1)
        # assert expect == result1

    def test_div(self):
        # self.calc = Calc()
        result = self.calc.div(2, 2)
        assert 1 == result


# test_pytest = Test_pytest()
# test_pytest.test_add_1(1, 2)

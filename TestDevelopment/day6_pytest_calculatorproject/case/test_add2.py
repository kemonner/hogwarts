"""
    题目：
        根据需求编写计算机器（加法和除法）相应的测试用例
        在调用每个测试方法之前打印【开始计算】
        在调用测试方法之后打印【结束计算】
        调用完所有的测试用例最终输出【结束测试】
        为用例添加标签
    注意：
        a、使用等价类，边界值，错误猜测等方法进行用例设计
        b、用例中要添加断言，验证结果
        c、灵活使用测试装置
"""
# 第二版实现的用例，工作中实现的代码
import allure
import pytest

from TestDevelopment.day6_pytest_calculatorproject.base.base1 import Base


@allure.feature("计算器测试用例")
class TestAdd2(Base):
    @allure.story("加法运算的P0测试用例")
    @pytest.mark.p0
    @pytest.mark.parametrize("x, y, expected", [(1, 1, 2), (-0.01, 0.02, 0.01), (10, 0.02, 10.02)])
    def test_add_p0(self, x, y, expected):
        with allure.step("调用加法函数"):
            print("p0调用加法函数")
            result = self.calculator.add(x, y)
            allure.attach.file(r"/Users/zxmac/Desktop/workspace/project/hogwarts/TestDevelopment/"
                               r"day6_pytest_calculatorproject/file/2022-11-16.png", name="屏幕截图",
                               attachment_type=allure.attachment_type.JPG, extension='.jpg')

        with allure.step("断言"):
            print("p0断言")
            allure.attach("这是一个文本格式")
            assert result == expected

    @allure.story("加法运算的P1测试用例")
    @pytest.mark.p1
    @pytest.mark.parametrize("x, y, expected", [(98.99, 99, 197.99), (99, 98.99, 197.99), (-98.99, -99, -197.99),
                                                (-99, -98.99, -197.99), (99.01, 0, "参数大小超出范围")])
    def test_add_p1(self, x, y, expected):
        with allure.step("P1测试用例断言"):
            assert self.calculator.add(x, y) == expected

    @allure.story("加法运算的P2测试用例")
    @pytest.mark.p2
    @pytest.mark.parametrize("x, y, expected", [(99.01, 0, "参数大小超出范围"), (-99.01, -1, "参数大小超出范围"),
                                                (2, 99.01, "参数大小超出范围"), (1, -99.01, "参数大小超出范围"),
                                                ("文", 9.3, "参数大小超出范围"), (4, "字", "参数大小超出范围")])
    def test_add_p2(self, x, y, expected):
        try:
            with allure.step("P1测试用例断言"):
                result = self.calculator.add(x, y)
        except TypeError as e:
            print(f"类型错误", {e})

        # with pytest.raises(TypeError) as e:
        #     result = self.calculator.add(x, y)
        # print(result, "1111", f"类型错误", {e})
        # assert e.type == TypeError



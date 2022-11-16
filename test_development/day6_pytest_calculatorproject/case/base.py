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
from test_development.day6_pytest_calculatorproject.script.calculator import Calculator


class Base:
    def setup(self):
        self.calculator = Calculator()
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")





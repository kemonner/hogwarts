from hogwarts.TestDevelopment.day6_pytest_calculatorproject.script.calculator import Calculator


class Base:
    def setup_class(self):
        # 调用calculator.py 中的add()方法
        # 实例化一个Calculator()实例
        self.calc = Calculator()

    def setup(self):
        # 测试装置，数据准备工作
        print("计算开始")

    def teardown(self):
        print("计算结束")

    def teardown_class(self):
        print("结束测试=====>")


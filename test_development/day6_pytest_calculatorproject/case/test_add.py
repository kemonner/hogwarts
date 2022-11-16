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
# 第一版实现用例，最简单的版本
import pytest
from test_development.day6_pytest_calculatorproject.script.calculator import Calculator


class TestAdd:
    def setup_class():
        print("开始计算")

    def teardown_class():
        print("结束计算")

    @pytest.mark.Ca_add_001
    @pytest.mark.parametrize("x, y, expect", [(1, 1, 2)])
    def test_add1(self, x, y, expect):
        self.calc = Calculator()
        assert x + y == expect

    @pytest.mark.Ca_add_002
    @pytest.mark.parametrize("x, y, expect", [(-0.01, 0.02, 0.01)])
    def test_add2(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_003
    @pytest.mark.parametrize("x, y, expect", [(10, 0.02, 10.02)])
    def test_add3(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_004
    @pytest.mark.parametrize("x, y, expect", [(98.99, 99, 197.99), (99, 98.99, 197.99), (-98.99, -99, -197.99), (-99, -98.99, -197.99), (99.01, 0, "参数大小超出范围")])
    def test_add4(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_005
    @pytest.mark.parametrize("x, y, expect", [(99, 98.99, 197.99)])
    def test_add5(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_006
    @pytest.mark.parametrize("x, y, expect", [(-98.99, -99, -197.99)])
    def test_add6(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_007
    @pytest.mark.parametrize("x, y, expect", [(-99, -98.99, -197.99)])
    def test_add7(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_008
    @pytest.mark.parametrize("x, y, expect", [(99.01, 0, "参数大小超出范围")])
    def test_add8(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_009
    @pytest.mark.parametrize("x, y, expect", [(-99.01, -1, "参数大小超出范围")])
    def test_add9(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_0010
    @pytest.mark.parametrize("x, y, expect", [(2, 99.01, "参数大小超出范围")])
    def test_add10(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_0011
    @pytest.mark.parametrize("x, y, expect", [(1, -99.01, "参数大小超出范围")])
    def test_add11(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_0012
    @pytest.mark.parametrize("x, y, expect", [("文", 9.3, "参数大小超出范围")])
    def test_add12(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

    @pytest.mark.Ca_add_0013
    @pytest.mark.parametrize("x, y, expect", [(4, "字", "参数大小超出范围")])
    def test_add13(self, x, y, expect):
        calc = Calculator()
        assert calc.add(x, y) == expect

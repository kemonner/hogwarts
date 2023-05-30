import pytest
# 通过绝对路径导入的包，才能在命令行执行时相互调用才不会报错
from hogwarts.TestDevelopment.day6_pytest_calculatorproject.base.base1 import Base
from hogwarts.TestDevelopment.day6_pytest_calculatorproject.log.log_util import logger


# 继承Base，在测试方法和用例执行前后输出开始计算，结束计算和结束测试
class TestAdd3(Base):
    # 使用mark分别标记，表及参数分开更细化
    @pytest.mark.add
    @pytest.mark.p0
    @pytest.mark.parametrize("x, y, expect", [(1, 1, 2), (-0.01, 0.02, 0.01), (10, 0.02, 10.02)])
    def test_add_p0(self, x, y, expect):
        result = self.calc.add(x, y)
        # 持久化日志输出
        logger.info(f"结果为: {result}")
        assert result == expect

    @pytest.mark.add
    @pytest.mark.p1
    @pytest.mark.parametrize("x, y, expect", [(98.99, 99, 197.99), (99, 98.99, 197.99), (-98.99, -99, -197.99),
                                              (-99, -98.99, -197.99)])
    def test_add_p1(self, x, y, expect):
        result = self.calc.add(x, y)
        logger.info(f"结果为: {result}")
        assert result == expect

    @pytest.mark.add
    @pytest.mark.p2
    @pytest.mark.parametrize("x, y, expect", [(99.01, 0, "参数大小超出范围"), (-99.01, -1, "参数大小超出范围"),
                                              (2, 99.01, "参数大小超出范围"), (1, -99.01, "参数大小超出范围"),
                                              ("文", 9.3, "参数大小超出范围"), (4, "字", "参数大小超出范围")])
    def test_add_p2(self, x, y, expect):
        try:
            result = self.calc.add(x, y)
        except TypeError as e:
            logger.info(f'类型错误为: {e}')


import pytest


# 1.不使用yaml外部参数化导入数据
# class TestData:
#     @pytest.mark.parametrize("a,b", [(10, 20), (20, 30)])
#     def testdata(self, a, b):
#         print(a+b)

# 2.使用yaml导入外部数据'
import yaml
#
#
# class TestData:
#     @pytest.mark.parametrize(("a", "b"),yaml.safe_load(open("./data.yaml")))
#     def testdata(self, a, b):
#         print(a+b)

# 3.获取yaml文件key值和value值还有全部内容
# 1.获取yaml文件key值
class TestData:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def testdata(self, env):
        if "test" in env:
            print("这是测试环境")
            # 2.获取yaml文件value值
            print("测试环境的ip是：", env["test"])
        elif "dev" in env:
            print("这是开发环境")
    # 3.获取yaml文件全部内容

    def testdata1(self):
        print(yaml.safe_load(open("./env.yaml")))

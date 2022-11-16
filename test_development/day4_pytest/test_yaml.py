import pytest
import yaml


# class DemoYaml:
# 读取dict格式yaml文件时，只获取Key值给env
@pytest.mark.parametrize('env', yaml.safe_load(open('/Users/zxmac/Desktop/workspace/project/hogwarts/test_development/'
                                                    'day4_pytest/demo_dict_param.yaml')))
def test_demo1(env):
    if 'test' in env:
        print('这是测试环境')
        print(env)
    elif 'dev' in env:
        print('这是开发环境')
        print(env)


# 只有读取list格式yaml文件时，可以获取到里面的全部内容
@pytest.mark.parametrize('env', yaml.safe_load(open('/Users/zxmac/Desktop/workspace/project/hogwarts/test_development/'
                                                    'day4_pytest/demo_list_param.yaml')))
def test_demo2(env):
    if 'test' in env:
        print('这是测试环境')
        print('测试环境的ip是：', env['test'])
    elif 'dev' in env:
        print('这是开发环境')
        print('开发环境的ip是：', env['dev'])


def test_demo3():
    # 当yaml格式是list格式时，才能读取到完整数据
    print(yaml.safe_load(open('/Users/zxmac/Desktop/workspace/project/hogwarts/test_development/day4_pytest/'
                              'demo_list_param.yaml')))


# if __name__ == '__main__':
#     dy = DemoYaml()
#     dy.test_demo1()
#     dy.test_demo2()
#     dy.test_demo3()

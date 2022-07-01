import allure
import pytest


# 第一步生成文件 python3 -m pytest test_allure_issure_link_demo1.py --alluredir=./result/test_allure_issure_link_demo1
# 第二步生成allure测试报告 allure serve ./result/test_allure_issure_link_demo1
@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass


TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.testcase(TEST_CASE_LINK, name='登录用例')
def test_with_testcase():
    print("这是一条测试用例链接，连接到你的测试用例里面")
    pass


@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass

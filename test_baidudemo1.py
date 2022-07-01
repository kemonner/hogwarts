import allure
import pytest
from selenium import webdriver
import time


@allure.testcase("http://www.baidu.com", name="测试用例")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data1", ["allure", "pytest", "unitest"])
def test_step_demo(test_data1):

    with allure.step("打开百度"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词: {test_data1},并搜索"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("截图保存"):
        driver.save_screenshot("./result/test_baidudemo1/a.png")
        allure.attach.file('./result/test_baidudemo1/a.png', name="截图", attachment_type=allure.attachment_type.PNG)
        allure.attach("<head></head><body>首页</body>", "Attach with HTML type", attachment_type=allure.attachment_type.HTML)

    with allure.step("关闭浏览器"):
        driver.quit()

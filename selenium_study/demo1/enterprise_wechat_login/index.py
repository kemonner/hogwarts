import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_study.demo1.enterprise_wechat_login import Login
from selenium_study.demo1.enterprise_wechat_login import Register


# 企业微信首页，登录和注册PO
class Index:
    # 访问地址
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")

    # 跳转到登录
    def goto_login(self):
        # click Login
        self._driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # 将self._driver传过去是因为不用再初始化一遍，使用已经初始化好的driver
        return Login(self._driver)

    # 跳转到注册页
    def goto_register(self):
        # click register
        self._driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        time.sleep(1)
        # 将self._driver传过去是因为不用再初始化一遍，使用已经初始化好的driver
        return Register(self._driver)

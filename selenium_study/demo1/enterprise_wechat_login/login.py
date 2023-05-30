from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_study.demo1.enterprise_wechat_login import Register


# 登录页除了扫码登录以外，也可以跳转到注册页
class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scan_qrcode(self):
        # scan qrcode
        pass

    def goto_register(self):
        # click register
        sleep(1)
        self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        # 将self._driver传过去是因为不用再初始化一遍，使用已经初始化好的driver
        return Register(self._driver)

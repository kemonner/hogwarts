import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    # 填写注册信息
    def register(self):
        time.sleep(2)
        self._driver.find_element(By.ID, "corp_name").send_keys("11111112222")
        self._driver.find_element(By.CSS_SELECTOR, "#corp_industry > a > span.ww_btn_Dropdown_label.js_corp_industry_"
                                                   "text").click()
        time.sleep(1)
        self._driver.find_element(By.CSS_SELECTOR, "#corp_industry > div > table > tbody > tr > td.register_industry"
                                                   "_wrap.register_industry_maintype_wrap > div:nth-child(1) > a").click()
        time.sleep(1)
        self._driver.find_element(By.CSS_SELECTOR, "#corp_industry > div > table > tbody > tr > td:nth-child(2) > div:"
                                                   "nth-child(1) > div:nth-child(3) > a").click()
        time.sleep(1)
        self._driver.find_element(By.ID, "manager_name").send_keys("阿三")
        time.sleep(3)
        self._driver.quit()
        # return True

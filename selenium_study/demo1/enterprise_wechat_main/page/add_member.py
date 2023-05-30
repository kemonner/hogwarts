from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

element = []
class AddMember:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def test_add_member(self):
        # sendkeys
        sleep(2)
        # self._driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()
        self._driver.find_element(By.ID, "username").send_keys(13312312318)
        # self._driver.find_element(By.ID, "memberAdd_english_name").send_keys("阿三")
        self._driver.find_element(By.ID, "memberAdd_acctid").send_keys(11223348)
        self._driver.find_element(By.ID, "memberAdd_biz_mail").send_keys("asan")
        self._driver.find_element(By.ID, "memberAdd_phone").send_keys(13312312318)
        sleep(1)
        self._driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form"
                                            "/div[3]/a[2]").click()
        sleep(2)
        # self._driver.quit()
        # return True

    def get_member(self):
        print("-----")
        elements = self._driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
        return [element.get_attribute("title") for element in elements]






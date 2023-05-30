from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import ddddocr
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

"""
1.启动浏览器
2.访问地址
3.登录后操作
"""


class AutoGet:
    # def setup(self):
    #     # self.options = Options()
    #     # self.options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome()
    #
    # def teardown(self):
    #     self.driver.quit()

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://69.234.195.70:81/")
        self.driver.maximize_window()
        time.sleep(2)

    def auto_get(self):
        print('***************正在加载必要元素，请耐心等待***************')
        # 输入账号密码
        self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[1]/div[3]/div/div[2]/"
                                          "form/div[1]/div/div/span/span/input").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[1]/div[3]/div/div[2]/"
                                          "form/div[1]/div/div/span/span/input").send_keys("admin")
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[1]/div[3]/div/div[2]/form"
                                          "/div[2]/div/div/span/span/input").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[1]/div[3]/div/div[2]/form"
                                          "/div[2]/div/div/span/span/input").send_keys("sandwich@123")
        time.sleep(0.5)
        # 获取验证码图片
        imgcode = self.driver.find_element(By.CSS_SELECTOR, "#userLayout > div > div.main > div > form > div.ant-tabs."
                                                            "ant-tabs-top.ant-tabs-line > div.ant-tabs-content."
                                                            "ant-tabs-content-animated.ant-tabs-top-content > div > "
                                                            "div:nth-child(2) > form > div:nth-child(3) > div.ant-col."
                                                            "ant-col-8 > img")
        # 识别后转变为文本
        ocr = ddddocr.DdddOcr()
        img_text = ocr.classification(imgcode.screenshot_as_png)
        # 将文本输入验证码输入框
        self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[1]/div[3]/div/div[2]/form/"
                                          "div[3]/div[1]/div/div/div/span/span/input").click()
        self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[1]/div[3]/div/div[2]/form/"
                                          "div[3]/div[1]/div/div/div/span/span/input").send_keys(img_text)
        # code = input("请输入验证码：")
        # time.sleep(10)
        # self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[1]/div[3]/div/div[2]/form/"
        #                                   "div[3]/div[1]/div/div/div/span/span/input").send_keys()
        # time.sleep(0.5)
        # 点击勾选自动登录
        # self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[2]/div/div/span/label"
        #                                   "/span[2]").click()
        # time.sleep(0.5)
        # 点击确定登录
        self.driver.find_element_by_xpath("//*[@id='userLayout']/div/div[2]/div/form/div[3]/div/div/span"
                                          "/button").click()
        time.sleep(3)
        # 点击邮件管理
        self.driver.find_element_by_xpath("//*[@id='app']/section/aside/div/ul/li[9]/a").click()
        time.sleep(0.5)
        a = 3
        while a > 0:
            # 点击新增邮件
            self.driver.find_element_by_xpath("//*[@id='app']/section/section/main/div[2]/div/div/div[2]/button[1]").click()
            time.sleep(0.5)
            # 填充邮件标题
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/"
                                              "form/div/div[1]/div/div[2]/div/span/input").click()
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/"
                                              "form/div/div[1]/div/div[2]/div/span/input").send_keys("道具迎新")
            # 填充邮件内容
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/form"
                                              "/div/div[2]/div/div[2]/div/span/textarea").click()
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/form"
                                              "/div/div[2]/div/div[2]/div/span/textarea").send_keys("道具迎新")
            # 选择发件人
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]"
                                              "/form/div/div[3]/div/div[2]/div/span/div/div[1]/input").click()
            # 从下拉选项中选择一个发件人
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, "body > div.el-select-dropdown.el-popper > div.el-scrollbar > "
                                                      "div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > "
                                                      "li:nth-child(2) > span").click()
            # 填入收件地址
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/form"
                                              "/div/div[5]/div/div[2]/div/span/input").click()
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/form"
                                              "/div/div[5]/div/div[2]/div/span/input").send_keys("0x5b0459900693a3b9d73b8f3"
                                                                                                 "299e0bf0ed33c3db9")
            # 选择道具类型邮件
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/form/div/div[6]/div/div[2]/div/span/div/div/input").click()
            time.sleep(1)
            # 下拉到底部
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 选择道具
            # WebDriverWait(self.driver, 10, 0.5).until(
            #     expected_conditions.presence_of_all_elements_located((By.XPATH, "/html/body/div[6]/div[1]/div[1]/ul/li[8]/span")))
            # time.sleep(0.5)
            self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(10) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(7)").click()
            time.sleep(0.5)
            # 备注随机填入1或者2
            num = random.randint(1, 2)
            time.sleep(0.5)
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/form"
                                              "/div/div[8]/div/div[2]/div/span/input").click()
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset[1]/form"
                                              "/div/div[8]/div/div[2]/div/span/input").send_keys(num)
            # 点击确定发送邮件
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
            a -= 1
        self.driver.quit()


if __name__ == "__main__":
    AutoGet().auto_get()



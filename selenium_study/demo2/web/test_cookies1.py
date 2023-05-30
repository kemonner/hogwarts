from selenium import webdriver
import time
import yaml
"""

    - 前置：打开浏览器
    1.拿到含有身份信息的cookie;
    2.拿到coookie后保存在本地文件中;
    3.将获取到的cookie信息写入到浏览器中，实现自动登录
    - 后置：关闭浏览器进程
    
"""


class TestGetCookies:
    # 启动浏览器
    def setup_class(self):
        """
        前置：启动浏览器
        :return:
        """
        self.driver = webdriver.Chrome()

    # 执行完毕关闭并退出
    def teardown_class(self):
        """
        后置：关闭浏览器进程
        :return:
        """
        self.driver.quit()

    def test_get_cookies(self):
        """
        1.拿到含有身份信息的cookie;
        2.拿到coookie后保存在本地文件中。
        :return:
        """
        # 访问企业微信
        self.driver.get("https://work.weixin.qq.com/")
        # 暂停30秒手动扫码登录
        time.sleep(30)
        # 获取cookie
        cookie = self.driver.get_cookies()
        # 保存cookie到yaml中
        with open("data.yaml", "w") as f:
            yaml.safe_dump(cookie, f)

    def test_add_cookies(self):
        """
        3.将获取到的cookie信息写入到浏览器中，实现自动登录
        :return:
        """
        # 先去访问企业微信官网，让代码知道你要把cookie信息加到哪里实现自动登录
        self.driver.get("https://work.weixin.qq.com/")

        # 获取cookie信息
        cookies = yaml.safe_load(open("data.yaml"))

        # 写入cookie信息
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # 重新请求主页就是登录状态了
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        time.sleep(10)
from selenium_study.demo1.enterprise_wechat_login import Index


# 启动代码
class TestRegister:
    def setup(self):
        self.index = Index()

    # 调用流程
    def testregister(self):
        self.index.goto_login().goto_register().register()
        self.index.goto_register().register()

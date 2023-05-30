from selenium import webdriver


class TestLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def setup_class(self):
        self.driver.get("http://69.234.195.70:81/")
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

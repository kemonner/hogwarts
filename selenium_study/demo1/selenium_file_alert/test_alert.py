from selenium.webdriver import ActionChains
from selenium_study.demo1.selenium_file_alert.base import Base
from selenium import webdriver
import time


class TestAlert(Base):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        time.sleep(1)

    def test_alert(self):
        """
        1.打开网页：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        2.操作窗口右侧页面frame，将元素1拖拽到元素2
        3.这是后会有一个alert弹框，点击弹框中的确定按钮
        4.然后再按'点击运行'
        5.关闭网页
        :return:
        """
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换到目标frame
        self.driver.switch_to.frame('iframeResult')

        # 需要拖拽的起始和终点
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(2)

    def teardown(self):
        self.driver.quit()

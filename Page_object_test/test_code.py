from Page_object_test.main import Main


class Test01:
    def use_code(self):
        # 用函数调用的方式实现页面操作流程，
        main = Main()
        # 这里用调用函数步骤的方法，实现从main脚本中调用first_click_link,return到搜索结果页面的操作脚本中去，搜索结果页面操作脚本
        # 中有对应的搜索结果页面的操作方法。
        # 用函数调用的方式实现页面的操作流程。
        # 这就是pageobject的主要原则。
        main.first_click_link().get_text()
        main.first_click_link().little_title()

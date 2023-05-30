from time import sleep

from selenium_study.demo1.enterprise_wechat_main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        get_member = self.main.test_add_member()
        get_member.test_add_member()
        sleep(2)
        assert "13312312318" in get_member.get_member()



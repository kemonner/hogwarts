import allure
import pytest


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>", attachment_type=allure.attachment_type.HTML)


# 图片调用的是file方法，文本和html默认调用的是call方法
def test_attach_photo():
    allure.attach.file("/Users/zxmac/Desktop/workspace/project/hogwarts/resource/huskeydog.jpeg", name="哈士奇",
                       attachment_type=allure.attachment_type.JPG)

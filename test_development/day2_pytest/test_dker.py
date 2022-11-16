import pytest


@pytest.mark.parametrize('wd', ['appium', 'selenium', 'pytest'])
@pytest.mark.parametrize('code', ['utf-8', 'gbk', 'gb2312'])
def test_dker(wd, code):
    print(f'wd: {wd}, code: {code}')

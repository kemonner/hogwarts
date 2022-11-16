import pytest

search_list = ['appium', 'selenium', 'pytest']


@pytest.mark.parametrize('name', search_list)
def test_search(name):
    assert name in search_list

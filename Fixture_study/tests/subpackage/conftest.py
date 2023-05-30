# content of tests/subpackage/conftest.py
import pytest


@pytest.fixture
def mid(order):
    print('b', 'sub')
    order.append("mid subpackage")
    print('c', order)

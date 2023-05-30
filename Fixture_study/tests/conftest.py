# content of tests/conftest.py
import pytest


@pytest.fixture
def order():
    print('s', 'top')
    return []


@pytest.fixture
def top(order, innermost):
    order.append("top")
    print(3, order)

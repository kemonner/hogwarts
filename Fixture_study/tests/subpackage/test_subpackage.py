# content of tests/subpackage/test_subpackage.py
import pytest


@pytest.fixture
def innermost(order, mid):
    print('a1', order)
    order.append("innermost subpackage")
    print('a', order)


def test_order(order, top):
    assert order == ["mid subpackage", "innermost subpackage", "top"]


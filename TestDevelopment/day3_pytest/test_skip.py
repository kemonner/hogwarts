import pytest


# 跳过代码
@pytest.mark.skip
def test_aaa():
    print("代码还没完成")
    assert True


# 跳过代码，显示原因
@pytest.mark.skip(reason='失败了')
def test_bbb():
    print("失败原因")
    assert False


def check_in():
    return False  # True


def test_ccc():
    print('start')
    if not check_in():
        pytest.skip(reason="不满足条件")
    print('end')






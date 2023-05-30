import pytest


# def test_raise():
    # 预期为ValueError异常
    # with pytest.raises(ValueError, match='must be 0 or None'):
    #     # 主动抛出ValueError异常，顺利通过
    #     raise ValueError("value must be 0 or None")

    # 预期为ValueError异常
    # with pytest.raises(ValueError, match='must be 0 or None'):
    #     # 结果主动抛出ZeroDivisionError异常，引发报错
    #     raise ZeroDivisionError("除数为0")

    # 预期为ValueError异常，预期的报错信息和引发的报错信息不一致
    # with pytest.raises((ZeroDivisionError, ValueError), match="must be 0 or None"):
    #     # 结果主动抛出ZeroDivisionError异常，引发报错
    #     raise ZeroDivisionError("除数为0")

    # 预期为ValueError异常，预期的报错信息和引发的报错信息一致
    # with pytest.raises((ZeroDivisionError, ValueError), match="除数为0"):
        # 结果主动抛出ZeroDivisionError异常，引发报错
        # raise ZeroDivisionError("除数为0")

def test_raise1():
    # 预期异常是ValueError
    with pytest.raises(ValueError) as exc_info:
        # 引发的异常是ZeroDivisionError
        raise ValueError("value must be 42")
    # 预期和引发的异常一致，所以并未引起异常，所以以下代码都可以被执行
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"
    print(exc_info.type)
    print(exc_info.value.args[0])
    print("-----")


# def test_raise2():
#     # 预期异常是ValueError
#     with pytest.raises(ValueError) as exc_info:
#         # 引发的异常是ZeroDivisionError
#         raise ZeroDivisionError("value must be 42")
#     # 预期和引发的异常不一致，导致出现异常，所以以下代码都不会被执行
#     assert exc_info.type is ValueError
#     assert exc_info.value.args[0] == "value must be 42"
#     print("-----")

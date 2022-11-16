def test_demo():
    a = 1
    b = 2
    expect = 3
    assert a + b == expect, "assert error"


def test_str():
    assert "abc" in "abcd"


import sys
def test_sys():
    print(sys.platform)
    assert ("linux" in sys.platform), "该代码只能在Linux下运行"


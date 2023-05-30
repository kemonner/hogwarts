import sys

import pytest

# 输出系统版本名称
# print(sys.platform)
# 如果系统版本名称是darwin，就输出reason里的描述
@pytest.mark.skipif(sys.platform == "darwin", reason='does not run on mac')
def test_case_a1():
    assert False
# 如果系统版本名称是win，就输出reason里的描述
@pytest.mark.skipif(sys.platform == "win", reason='does not run on weindows')
def test_case_b2():
    assert True
# 输出当前使用应用版本信息
print(sys.version_info)
# 如果当前系统版本小于6,9，就输出reason里的描述
@pytest.mark.skipif(sys.version_info > (6,9), reason='requires python3.6 or higher')
def test_case_c3():
    assert False

print(__name__)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pytestTest
# @File     :testassert
# @Date     :2021/1/15 12:00
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""

import pytest
class TestAssert(object):

    # def test_001(self):
    #     print("test001执行了")
    #     value = 1 % 2
    #     assert value == 0, 'value 不是偶数是奇数'

    def test_zero_division(self):
        print("test002执行了")
        with pytest.raises(ZeroDivisionError) as info:
            1/0
        # assert info.type == 'RuntimeError'
        assert info.type == "<class 'ZeroDivisionError'>"

    def test_003(self):
        print("test003执行了")

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pytestTest
# @File     :testskip
# @Date     :2021/1/15 11:33
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""

import pytest
class TestSkip(object):

    # 无条件跳过
    @pytest.mark.skip('无条件跳过')
    def test_001(self):
        print("test001执行了")

    @pytest.mark.skipif(1<2, reason="条件成立，跳过执行")
    def test_002(self):
        print("test002执行了")

    def test_003(self):
        print("test003执行了")
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pytestTest
# @File     :testxfail
# @Date     :2021/1/15 11:38
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""

# 无条件跳过
import pytest

class TestXfail():
    @pytest.mark.xfail('无条件标记预期失败')
    def test_001(self):
        print("test001执行了")

    @pytest.mark.xfail(1<2,'条件成立，标记预期失败')
    def test_002(self):
        print("test002执行了")

    def test_003(self):
        print("test003执行了")

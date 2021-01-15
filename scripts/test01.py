# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pytestTest
# @File     :test01
# @Date     :2021/1/11 10:26
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pytest
class Test01(object):
    def setup_class(self):
        print("类初始化")

    def teardown_class(self):
        print("类结束")

    def setup(self):
        print("方法初始化")

    def teardown(self):
        print("方法结束")

    def test_001(self):
        print("test001执行了")

    def test_002(self):
        print("test002执行了")



# if __name__ == '__main__':
#     print("条件成立")
#     pytest.main( "test01.py" )
# else:
#     print("条件不成立没被执行")

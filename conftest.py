# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pytestTest
# @File     :conftest.py
# @Date     :2021/1/15 10:59
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pytest
@pytest.fixture(scope='session')
def username():
    print('\n获取用户名,scope为session级别多个.py模块只运行一次')
    a = 'wulimin'
    return a
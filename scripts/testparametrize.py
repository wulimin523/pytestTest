# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pytestTest
# @File     :testparametrize
# @Date     :2021/1/15 11:43
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pytest
class TestParametrize():
    # 单个参数：@pytest.mark.parametrize("参数名",[参数值])，执行次数为参数值列表的元素个数
    @pytest.mark.parametrize('username', ['wulimin', 'guoyangyang', 'guolili'])
    def test01(self, username):
        print('用户名为：', username)
        print('test01执行了')

    # 多个参数：pytest.mark.parametrize("参1,参2,参3,...",[(值1,值2,值3,...)])。格式必须为列表嵌套元祖，如果多组数据，使用不同的元祖分隔
    @pytest.mark.parametrize( 'username,age,address', [('wulimin',32,'濮阳'), ('guoyangyang',3,'郑州'), ('guolili',32,'邓州')] )
    def test02(self, username, age, address):
        print( '用户名、年龄，地址依次为：', username, age, address )
        print( 'test01执行了' )
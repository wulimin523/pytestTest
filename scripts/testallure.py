# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pytestTest
# @File     :testallure
# @Date     :2021/1/15 15:39
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""

import allure
import pytest
import utils


@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
def test001():
    '''
    测试用例001
    '''
    print('test01执行了')

@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('critical')
def test002():
    '''
    测试用例002
    '''
    print('test02执行了')

@allure.feature( 'test_module_01' )
@allure.story( 'test_story_01' )
@allure.severity( 'critical' )
def test0022():
    '''
    测试用例0022
    '''
    print( 'test022执行了' )

@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('normal')
def test003():
    '''
    测试用例003
    '''
    print('test03执行了')

@allure.feature('test_module_02')
@allure.story('test_story_01')
@allure.severity('minor')
def test004():
    '''
    测试用例004
    '''
    print('test04执行了')

@allure.feature('test_module_02')
@allure.story('test_story_02')
@allure.severity('trivial')
def test005():
    '''
    测试用例005
    '''
    print('test05执行了')


class TestShoppingTrolley( object ):
    @allure.story( '加入购物车' )  # story定义用户场景
    def test_add_shopping_trolley(self):
        login( '刘春明', '密码' )  # 调用“步骤函数”
        with allure.step( "浏览商品" ):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤2
            allure.attach( '商品1', '刘春明' )  # attach可以打印一些附加信息
            allure.attach( '商品2', 'liuchunming' )
        with allure.step( "点击商品" ):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤3
            pass
        # with allure.step("查看图片"):
        #     file = open(utils.BASE_DIR + '/image/apple.jpg', 'rb').read()
        #     allure.attach('apple', file, allure.attachment_type.JPG)
        with allure.step( "校验结果" ):
            allure.attach( '期望结果', '添加购物车成功' )
            allure.attach( '实际结果', '添加购物车失败' )
            assert 'success' == 'failed'

    @allure.story( '修改购物车' )
    def test_edit_shopping_trolley(self):
        pass

    @pytest.mark.skipif( reason='本次不执行' )
    @allure.story( '删除购物车' )
    def test_delete_shopping_trolley(self):
        pass

@allure.step('用户登录')  # 还可以将一个函数作为一个步骤，调用此函数时，报告中输出一个步骤，步骤名字通常是函数名，我把这样的函数叫“步骤函数”
def login(user, pwd):
    print(user, pwd)



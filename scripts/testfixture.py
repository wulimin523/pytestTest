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
# 参考文档：https://www.cnblogs.com/yoyoketang/p/9762197.html
import pytest

@pytest.fixture()
def fun1():
    print("我是工厂函数1")

@pytest.fixture()
def fun2():
    print('我是工厂函数2')

@pytest.fixture()
def funreturn():
    print("我是带返回值的工厂函数")
    return 2
# fixture为module级别时，在当前.py脚本里面所有用例开始前只执行一次
@pytest.fixture(scope='module', autouse=True)
def funmodule():
    print("适用于module的工厂函数")

# fixture为class级别的时候，如果一个class里面有多个用例，都调用了此fixture，那么此fixture只在该class里所有用例开始前执行一次
@pytest.fixture(scope='class', autouse=True)
def funclass():
    print("适用于class的工厂函数")

# @pytest.fixture()如果不写参数，默认就是scope="function"，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例运行之后运行。
@pytest.fixture(scope='function', autouse=True)
def funfunction():
    print("适用于function的工厂函数")

# 工厂函数修饰中params参数，使用内置参数request及操作 如：request.param
# 特色：params值为列表，列表中有几个值，调用工厂函数的测试方法，会被执行几次。
@pytest.fixture(params=[1, 2, 3])
def funparam(request):
    print('带有参数的工厂函数')
    return request.param

def test_a():
    print("我是函数a")


class TestFixture(object):
    # def setup_class(self):
    #     print("类初始化2")
    #
    # def teardown_class(self):
    #     print("类结束2")
    #
    # def setup(self):
    #     print("方法初始化2")
    #
    # def teardown(self):
    #     print("方法结束2")

    # 参数方式调用工厂函数
    def test_001(self, fun1):
        print("test001执行了")

    # 函数方式调用工厂函数
    @pytest.mark.usefixtures('fun1')
    def test_002(self):
        print( "test002执行了" )

    def test_003(self):
        print("test003执行了")

    # 如果一个方法或者一个class用例想要同时调用多个fixture，可以使用@pytest.mark.usefixture()进行叠加。
    # 注意叠加顺序，先执行的放底层，后执行的放上层
    @pytest.mark.usefixtures( 'fun2' )
    @pytest.mark.usefixtures('fun1') #放在下层的先执行
    def test_004(self):
        print("test004执行了")

    # 如果工厂函数带返回至，只能通过参数的方式调用工厂函数，不能用@pytest.mark.usefixtures
    def test_005(self, funreturn):
        a = funreturn + 2
        print('a=', a)
        print("test005执行了")

    # fixture为session级别是可以跨.py模块调用的,也就是当我们有多个.py文件的用例时候，
    # 如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里
    # conftest.py文件名称是固定的，pytest会自动识别该文件。
    # 放到工程的根目录下，就可以全局调用了，如果放到某个package包下，那就只在该package内有效
    def test_006(self, username):
        print('登录的用户名为：', username)
        print('test006执行了')
    # 如果多个用例只需调用一次fixture,test_006已调用过，此函数不再调用
    def test_007(self, username):
        print( '登录的用户名为：', username )
        print( 'test007执行了' )

    # 工厂函数修饰中params参数，工厂函数的参数列表中有几个值，调用工厂函数的测试方法，会被执行几次。
    def test_008(self, funparam):
        print('参数：', funparam)
        print('test008执行了')





# if __name__ == '__main__':
#     print("条件成立")
#     pytest.main( "test02.py" )
# else:
#     print("条件不成立没被执行")

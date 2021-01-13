# -*- coding: utf-8 -*-
import company
import person
import mock
import os
zhangsan = person.Person("zhang san")
shoeshop = company.Company("the shop",zhangsan)

# print (zhangsan.get_name())
# print (shoeshop.who_is_boss())

# 场景01：永远返回我们想要的值
# 关键词：return_value
# 支持的类型
# zhangsan.get_name = mock.Mock(return_value = "li si")
# print(shoeshop.who_is_boss())
# zhangsan.get_name = mock.Mock(return_value = 12345)
# print(shoeshop.who_is_boss())
# zhangsan.get_name = mock.Mock(return_value = [2,'4',6])
# print(shoeshop.who_is_boss())

# 场景03：根据调用次数返回想要的结果。
# 关键词： side_effect
# 超出调用次数时抛出Stoplteration异常
# zhangsan.get_name = mock.Mock(side_effect=["li si",12345])
# print (shoeshop.who_is_boss())
# print (shoeshop.who_is_boss())
# print (shoeshop.who_is_boss())

# 场景04：根据参数返回想要的结果
# 关键词： side_effect
# 实现方式：替换函数逻辑
# def new_logic(arg):
#     paris = {
#         'a' : 123,
#         True : 'abc'
#     }
#     return paris[arg]
# zhangsan.get_name = mock.Mock(side_effect=new_logic)
# print(zhangsan.get_name(True))
# print(zhangsan.get_name('a'))

# 场景05： 抛出想要的异常或错误。
# 关键词： side_effect
# zhangsan.get_name = mock.Mock(side_effect=KeyError("keyerror"))
# print (shoeshop.who_is_boss())

# 场景06： 限制mock作用域
# 关键词： with、patch.object
# print (shoeshop.who_is_boss())
# with mock.patch.object(person.Person,'get_name',return_value = "li si"):
#     print(shoeshop.who_is_boss())
# print (shoeshop.who_is_boss())

# 场景07：获取调用信息
# 在本例中：
#     函数是否被调用：called
#     函数被调用次数：call_count
#     函数被调用的形式：call_args、call_args_list
# zhangsan.get_name = mock.Mock(side_effect=zhangsan.get_name)
# print(zhangsan.get_name.called)
# print(zhangsan.get_name.call_count)
# print(zhangsan.get_name.call_args)
# print(zhangsan.get_name.call_args_list)

# print(shoeshop.who_is_boss())
# print(shoeshop.who_is_boss())
# print(shoeshop.who_is_boss())

# print(zhangsan.get_name.called)
# print(zhangsan.get_name.call_count)
# print(zhangsan.get_name.call_args)
# print(zhangsan.get_name.call_args_list)

# 场景08：在返回值改变的同时，确保api不会因mock而改变
# 关键词：create_autospec
# shoeshop.who_is_boss = mock.create_autospec(shoeshop.who_is_boss,return_value="li si")
# print (shoeshop.who_is_boss())
# print (shoeshop.who_is_boss('abc'))

# 场景09：从零构造依赖模块。
# 适用于依赖模块只定义了接口，但尚未开发的场景
# zhangsan = mock.Mock()
# zhangsan.get_name = mock.Mock(return_value='zhang san')
# shoeshop = company.Company('the shop',zhangsan)
# print (shoeshop.who_is_boss())

# 场景10： 替换函数调用链。
# 函数调用链：
#     os.popen(cmd).read().split()
# Mock方法：
#     os.popen = mock.Mock()
#     os.popen.return_value.read.return_value.split.return_value = xx
print(os.popen('hostname').read().split())
os.popen = mock.Mock()
os.popen.return_value.read.return_value.split.return_value = 'mock'
print (os.popen('hostname').read().split())
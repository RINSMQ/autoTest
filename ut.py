# -*- coding: utf-8 -*-
import unittest
import person
import company

class PersonTestCase(unittest.TestCase):
    # 针对Person类的测试
    def setUp(self):
        self.p1 = person.Person("zhang san")
        self.p2 = person.Person("li si")
    # 测试函数必须以 test 开头
    def test_get_name(self):
        # 获取名字
        self.assertEqual(self.p1.get_name(), "zhang san")
        self.assertEqual(self.p2.get_name(), "li si")

# 必须继承字unittest
class CompanyTestCase(unittest.TestCase):
    # 装饰器
    @classmethod 
    def setUpClass(self):
        self.boss = person.Person("zhang san")
        self.kfc = company.Company("KFC",self.boss)
    
    def tearDown(self):
        self.kfc.staffs.clear()

    def test_who_is_boss(self):
        self.assertEqual(self.kfc.who_is_boss(),"zhang sn")

    def test_number_of_staffs_increase_when_hire_different_name_person(self):
        self.kfc.hire(person.Person("li si"))
        self.assertEqual(len(self.kfc.staffs),1)
        self.kfc.hire(person.Person("wang wu"))
        self.assertEqual(len(self.kfc.staffs),2)
    
    def test_number_of_staffs_not_change_when_hire_same_name_person(self):
        self.kfc.hire(person.Person("wangwu"))
        self.assertEqual(len(self.kfc.staffs),1)
        self.kfc.hire(person.Person("wangwu"))
        self.assertEqual(len(self.kfc.staffs),1)
    
def MyTestSuite():
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(PersonTestCase("test_get_name"))
    suite.addTest(CompanyTestCase("test_who_is_boss"))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="MyTestSuite")



'''
执行输入
    .  ： 测试正确
    F  ： 测试失败
    E  ： 异常中断
'''

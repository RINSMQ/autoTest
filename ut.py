# -*- coding: utf-8 -*-
import unittest
import person

class PersonTestCase(unittest.TestCase):
    # 针对Person类的测试
    def setUp(self):
        self.p1 = person.Person("zhang san")
        self.p2 = person.Person("li si")
    # 测试函数必须以 test 开头
    def test_get_name(self):
        # 获取名字
        self.assertEqual(self.p1.get_name(), "zhang san")
        self.assertEqual(self.p2.get_name(), "lisi")


if __name__ == "__main__":
    unittest.main()
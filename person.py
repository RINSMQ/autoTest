import os
class Person(object):
    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        # 获取姓名
        return self.name
# -*- coding: utf-8 -*-
class Company(object):
    def __init__(self,name,boss):
        self.name = name
        self.boss = boss
        self.staffs = set()
    def who_is_boss(self):
        return self.boss.get_name()

    def hire(self, person):
        self.staffs.add(person.get_name())
    
    def fire(self,person):
        pass
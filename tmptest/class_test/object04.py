#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person:
    name = '张三'

    def eat(self):
        print('{}正在学习'.format(Person.name))  # 类属性
        print('{}正在学习'.format(self.name))  # 对象属性


p1 = Person()
p1.name = '李四'
p1.eat()

p2 = Person()
p2.name = '王五'
p2.eat()

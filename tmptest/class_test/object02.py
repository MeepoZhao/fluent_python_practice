#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
定义类和属性

先找对象属性，然后找类属性
"""


class Student:
    name = 'xiaohua'
    age = 18


xiao = Student()
xiao.gender = 'male'  # 对象属性
xiao.age = 24
print(xiao.gender)
print(xiao.age)

xx = Student()
print('xx.age = ', xx.age)

Student.age = 10
print('xx.age = ', xx.age)
print('xiao.age = ', xiao.age)

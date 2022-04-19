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
xiao.age = 24  # 对象属性
print(xiao.gender)
print(xiao.age)

xx = Student()
print('xx.age = ', xx.age)  # 此处xx对象未创建属性，就会去类中寻找相关属性

Student.age = 10  # 此处修改了类的属性值
print('xx.age = ', xx.age)  # 此处返回的是类中的属性值
print('xiao.age = ', xiao.age)  # xiao对象中有age属性，故此处返回的是xiao对象中age属性的值

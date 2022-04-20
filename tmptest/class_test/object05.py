#!/usr/bin/python
# -*- coding: utf-8 -*-

# 类方法
"""
特征：
    1、在对象创建之前就存在，可以直接使用类调用该方法
    2、传递的参数是类，而非对象
    3、只可以使用类属性，不能使用对象属性，因为该方法的加载时间是早于对象的创建时间
    4、类方法中不能访问普通方法

类方法作用：
    1、类似于Java中的静态方法
    2、修改类属性

静态方法：
    1、需要装饰器@staticmethod
    2、无需传递参数
    3、也只能访问类的属性和方法，对象的是无法访问的
    4、加载时间同类方法
"""


class Dog:
    __age = 2

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):
        print('{}在院子里跑来跑去'.format(self.nickname))

    @classmethod  # 类方法装饰器
    def test(cls):  # cls指类
        print(cls)
        print(cls.__age)

    @staticmethod  # 静态方法，与类方法不同点在于,不需要传递一个类参数
    def test():
        print(Dog.__age)


dog1 = Dog('大黄')
dog1.run()

dog1.test()

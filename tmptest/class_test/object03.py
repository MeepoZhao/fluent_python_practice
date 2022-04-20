#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
类的方法
    self参数：指的是类的实例

"""


class Phone:
    brand = 'xiaomi'  # 类的属性

    # price = 3999

    def __init__(self, price: int) -> None:  # 初始化动作，创建对象时会执行
        self.price = price  # 对象的属性

    def call(self):
        print('self-------->', self)
        print('正在打电话')

    def get_price(self):  # self参数是指对象，即类的实例
        print('手机价格是:', self.price)


phone1 = Phone(2999)
print(phone1)
phone1.call()  # call(phone1)，此处类中函数定义的self指的是phone1
phone1.price = 5000
phone1.get_price()
phone1.brand = 'iphone'  # 将属性brand动态绑定到phone1对象上
print(phone1.brand)
phone2 = Phone(6777)
print(phone2.brand)


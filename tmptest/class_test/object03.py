#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
类的方法
    self参数：指的是类的实例

"""


class Phone:
    brand = 'xiaomi'
    price = 3999

    def call(self):
        print('self-------->', self)
        print('正在打电话')

    def get_price(self):  # self参数是指对象，即类的实例
        print('手机价格是:', self.price)


phone1 = Phone()
print(phone1)
phone1.call()  # call(phone1)，此处类中函数定义的self指的是phone1
phone1.price = 5000
phone1.get_price()

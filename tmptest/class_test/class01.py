#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/13

class Motor:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def built_car(self, name, color):
        self.name = name
        self.color = color

    def showMessage(self):
        print('款式:{0:6s}, 颜色:{1:4s}'.format(self.name, self.color))


# car1 = Motor()
# car1.built_car('Altiss', '红色')
# car1.showMessage()
print("====================")
car2 = Motor('Vios', '蓝色')
car2.showMessage()

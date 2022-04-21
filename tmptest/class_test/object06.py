#!/usr/bin/python
# -*- coding: utf-8 -*-

# 魔术方法

class Person:
    def __init__(self, name):
        print('-------> init ')
        self.name = name

    def __new__(cls, name):  # 该函数负责向内存申请地址
        print('---------> new ')
        return super().__new__(cls)  # 此时的 return 是将新开辟的地址返回给 __init__函数

    def __call__(self, *args, **kwargs):  # 将对象按照函数的方式调用会触发该方法 p()
        print('------> call ')

    # 删除变量和地址之间的引用关系，当一块空间没有任何引用时，会执行该函数
    # python解释器会在执行完该脚本后，释放所有内存空间，此时也会执行该函数
    def __del__(self):
        print('-------> del')


p = Person('jack')  # 先执行__new__，然后再执行 __init__，然后将内存地址绑定到参数p上
p()  # 该调用会触发 __call__方法

p1 = p
p2 = p

del p1  # 此时会执行变量和内存断开操作，是否会执行__del__函数取决于该内存是否还有变量引用

n = 5
print('n的值是:', n)

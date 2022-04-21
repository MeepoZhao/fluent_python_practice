#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/21

# 使用内省单独的模块来获取所有的函数，但需要将相关的函数都写入到一个模块中
import inspect
from collections import namedtuple

# 定义客户类
Customer = namedtuple('Customer', 'name fidelity')


# 定义商品类
class LineItem:
    # 初始化
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    # 计算商品的总价
    def total(self):
        return self.quantity * self.price


class Order:
    # 初始化
    def __init__(self, customer: Customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    # 计算总价 = 购物篮各个商品的总价
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    # 计算折后金额
    def due(self):
        discount = 0
        if self.promotion is not None:
            discount = self.promotion(self)
        return self.total() - discount

    # 打印出Order的结果
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


if __name__ == '__main__':
    joe = Customer('John', 0)
    ann = Customer('Ann', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]

    import promotions

    promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]


    def best_promo(order: Order):
        return max(promo(order) for promo in promos)


    print(Order(ann, cart, best_promo))

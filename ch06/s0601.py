#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/21

from abc import ABC, abstractmethod
from collections import namedtuple

# 生成一个客户类，包括客户姓名和客户积分数值
Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    # 对象初始化，生成一个包含产品名称、数量和单价的对象
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    # 实现一个计算总费用的函数
    def total(self):
        return self.price * self.quantity


class Order:
    # 初始化一个订单对象，传入的参数包括 客户对象，购买的商品清单，使用的促销方案
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    # 计算一个订单的总和 = 购物车中所有商品的总和
    def total(self):
        if not hasattr(self, '__total'):  # 此处为何使用该判断？害怕命名覆盖
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)  # 调用promotion对象中实现的discount函数
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# 定义一个抽象基类，继承该类的，需要实现@abstractmethod装饰的函数
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromo(Promotion):
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.7
        return 0


if __name__ == '__main__':
    joe = Customer('John', 0)
    ann = Customer('Ann', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    print(Order(joe, cart, FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))

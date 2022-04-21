#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/21

# 使用函数方法对s0601中的代码进行重构，以取代使用类

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


# 实现各个promotion的函数
def fidelity_promo(order: Order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order: Order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order: Order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


if __name__ == '__main__':
    joe = Customer('John', 0)
    ann = Customer('Ann', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    # print(Order(joe, cart, fidelity_promo))
    # print(Order(ann, cart, fidelity_promo))

    # 计算最佳折扣
    promos = [fidelity_promo, bulk_item_promo, large_order_promo]


    def best_promo(order: Order):
        return max(promo(order) for promo in promos)

    print(Order(ann, cart, best_promo))

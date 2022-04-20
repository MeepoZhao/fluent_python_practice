#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/19

def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s = "%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def f(a: int, *, b: int) -> tuple:
    """
    定义函数时，若想指定仅限关键字参数，要把他们放在前面有*的参数后面。
    如果不想支持数量不定的定位参数，但是想支持仅限关键字参数，在签名中放一个*
    仅限关键字参数不一定要有默认值，可以按照该函数定义的方式，强制必须传入实参
    注解：
    参数a和b冒号后面的类型是注解， -> tuple 是返回值的注解
    Python对注解所做的唯一的事情是，把他们存储在函数的__annotations__属性里
    Python不做检查、不做强制、不做验证、什么操作都不做，即注解对Python解释器没有任何意义
    :param a:
    :param b:
    :return:
    """
    return a, b


if __name__ == '__main__':
    # print(tag('br'))  # name = 'br'
    # print(tag('p', 'hello'))  # name = 'p',content = ['hello']
    # print(tag('p', 'hello', 'world'))  # name = 'p',content = ['hello','world']
    # print(tag('p', 'hello', id=33))  # name = 'p',content = ['hello'],attrs = {'id':33}
    # print(tag('p', 'hello', 'world', cls='sidebar'))  # name='p',content=['hello','world'],cls='sidebar'
    # print(tag(content='testing', name='img'))  # name='img',attrs={'content':'testing'}
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    # print(tag(**my_tag))  # 字典中所有元素作为单个参数传入，同名的键会绑定到对应的具名参数上，余下的会被attrs捕获
    # print(f(1, b=2))  # 调用f(1, 2)会报错：f() takes 1 positional argument but 2 were given

    # 把函数的签名绑定到一个参数字典上
    import inspect

    sig = inspect.signature(tag)
    bound_args = sig.bind(**my_tag)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)

    # 获取函数的注解
    print(f.__annotations__)
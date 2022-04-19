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


if __name__ == '__main__':
    # print(tag('br'))  # name = 'br'
    # print(tag('p', 'hello'))  # name = 'p',content = ['hello']
    # print(tag('p', 'hello', 'world'))  # name = 'p',content = ['hello','world']
    # print(tag('p', 'hello', id=33))  # name = 'p',content = ['hello'],attrs = {'id':33}
    # print(tag('p', 'hello', 'world', cls='sidebar'))  # name='p',content=['hello','world'],cls='sidebar'
    print(tag(content='testing', name='img'))  # name='img',attrs={'content':'testing'}

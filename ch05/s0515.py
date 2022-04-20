#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/20


def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断字符串"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)  # rfind()，用于查找字符串中sub的index
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)

    return text[:end].rstrip()


if __name__ == '__main__':
    # print(clip.__defaults__)
    # print(clip.__code__)
    # print(clip.__code__.co_varnames)  # 获取函数中的变量清单
    # print(clip.__code__.co_argcount)  # 获取函数的参数个数
    # 提取函数签名
    from inspect import signature

    sig = signature(clip)
    print(sig)
    print(str(sig))
    print('=============>')
    for name, parm in sig.parameters.items():
        print(parm.kind, ':', name, '=', parm.default)

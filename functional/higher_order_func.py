#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt


# 高阶函数英文是：higher-order function
# 一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数


def same(x, *fs):
    s = [f(x) for f in fs]
    return s


print(same(2, sqrt, abs))

print()


def do_sth(x=None, *func):
    if x is None:
        x = []
    return [f(xk) for xk in x for f in func]


print(do_sth([1, 2, 4, 9], abs, sqrt))

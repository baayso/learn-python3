#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_odd(n):
    return n % 2 == 1


L = range(100)

# 删掉偶数，只保留奇数
print(list(filter(is_odd, L)))

print()


def not_empty(s):
    return s and s.strip()


# 把一个序列中的空字符串删掉
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

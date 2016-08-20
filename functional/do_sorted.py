#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 对list进行排序
print(sorted([36, 5, -12, 9, -21]))

# 自定义排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 忽略大小写的字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 反向忽略大小写的字符串排序，传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

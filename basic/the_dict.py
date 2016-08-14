#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])

print()

# 增加
d['Adam'] = 67
print(d)
print(d['Adam'])

print()

# 替换
d['Jack'] = 90
print(d)
d['Jack'] = 88
print(d)

print()

# 使用in判断key是否存在
print('Thomas' in d)

# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))

print()

# 删除
print(d)
val = d.pop('Bob')
print(val)
print(d)

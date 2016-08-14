#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合
# s = set([1, 2, 3])
s = {1, 2, 3}
print(s)

print()

# 重复元素在set中自动被过滤
# s = set([1, 1, 2, 2, 3, 3])
s = {1, 1, 2, 2, 3, 3}
print(s)

print()

# 添加元素
s.add(4)
s.add(4)
print(s)

print()

# 删除元素
s.remove(4)
print(s)

print()

# s1 = set([1, 2, 3])
s1 = {1, 2, 3}
# s2 = set([2, 3, 4])
s2 = {2, 3, 4}
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)

print()

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
# 所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

# 试试把list放入set，看看是否会报错。
# s = set([0, [1], [2]])
# print(s)

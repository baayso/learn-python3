#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# tuple没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

print()

# 空tuple
t = ()
print(t)
print(len(t))

print()

# 下面不是定义tuple，是数学公式中的小括号
t = (1)
print(t)

# 定义只有1个元素的tuple时必须加一个逗号,
t = (1,)
print(t)

print()

# “可变的”tuple
# 其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

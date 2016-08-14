#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

print()

# 追加元素到末尾
classmates.append('Adam')
print(classmates)

print()

# 把元素插入到指定的位置
classmates.insert(1, 'Jack')
print(classmates)

print()

# 删除list末尾的元素
classmates.pop()
print(classmates)
print()

# 删除指定位置的元素
classmates.pop(1)
print(classmates)

print()

# 把某个元素替换成别的元素，直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

print()

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)

print()

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s)
print(len(s[2]))
print(s[2][1])

print()

# 注意s只有4个元素，其中s[2]又是一个list
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(len(s))
print(s)

print()

# 空list
L = []
print(len(L))

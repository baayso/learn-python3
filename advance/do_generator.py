#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一边循环一边计算的机制，称为生成器：generator

# 只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

print()

# generator也是可迭代对象
for x in g:
    print(x)

print()


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# generator和函数的执行流程不一样
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# generator是在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b  # 相当于 t = (b, a + b); a = t[0]; b = t[1]
        n += 1
    return 'done'


print(fib(6))
# 使用for循环迭代generator，不使用繁琐的next()来获取下一个返回值
for n in fib(6):
    print(n)

print()

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print()


# generator是在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
next(o)
next(o)
next(o)

# 小结
# Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
# 请注意区分普通函数和generator函数，普通函数调用直接返回结果；
# generator函数的“调用”实际返回一个generator对象。

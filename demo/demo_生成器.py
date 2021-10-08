import sys


def fibonacci(n): # 生成器函数 - 斐波那契 数列
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        pass
        
        yield a  # 暂停运行并返回当前参数的值
        a, b = b, a + b
        counter += 1
    pass
pass
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        break
    pass
pass
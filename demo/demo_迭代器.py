import sys

list = [1,2,3,4,5,6,7,8,9,10]

it = iter(list) #创建迭代器

while True:
    try:
        print(next(it))
    
    except StopIteration:  #捕获迭代停止异常，并结束循环
        print("迭代结束")
        break
pass

'''
    将类作为迭代器
'''
class MyNumbers: 
    def __iter__(self):  #自定义获取迭代对象的方法
        self.a = 1
        return self
    pass

    def __next__(self): #获取下一个的方法
        x = self.a
        if x <= 20:
            self.a += 1
        else:
            '''
                StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况
            '''
            raise StopIteration
        return x
    pass
pass

 
myClass = MyNumbers()
myIter = iter(myClass)
 
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))